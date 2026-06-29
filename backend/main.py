from fastapi import FastAPI, UploadFile, File
from pathlib import Path
import uuid
from datetime import datetime
import shutil
from agents.project_reader import ProjectReader
from agents.review_coordinator import ReviewCoordinator
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from backend.database.review_store import ReviewStore
from pydantic import BaseModel

class GithubRequest(BaseModel):
    repo_url: str

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.get("/")
def home():
    return {"message": "Welcome to AI Software Engineering Reviewer"}

@app.post("/upload")
async def upload_project(file: UploadFile = File(...)):
    
    upload_id = f"{uuid.uuid4()}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    project_folder = UPLOAD_DIR / upload_id
    project_folder.mkdir()

    zip_path = project_folder / "original.zip"

    with open(zip_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    reader = ProjectReader(upload_id)

    extract_folder = reader.extract_zip()

    project_files = reader.read_project_files()

    coordinator = ReviewCoordinator(project_files, extract_folder)

    report = coordinator.run()

    report["id"] = str(uuid.uuid4())
    
    report["created_at"] = datetime.now().strftime("%d-%m-%Y %H:%M")

    store = ReviewStore()

    store.save(report)

    return {
        "message": "Project uploaded successfully",
        "upload_id": upload_id,
        **report,
        "total_files": len(project_files),
    }

@app.get("/download-report")
def download_report():

    return FileResponse(
        "review_report.pdf",
        media_type="application/pdf",
        filename="AI_Review_Report.pdf"
    )

@app.get("/reviews")
def get_reviews():

    store = ReviewStore()

    return store.get_all()

@app.delete("/reviews/{review_id}")
def delete_review(review_id: str):

    store = ReviewStore()

    store.delete(review_id)

    return {
        "message": "Review deleted successfully"
    }

@app.get("/stats")
def get_stats():

    store = ReviewStore()

    reviews = store.get_all()

    if not reviews:
        return {
            "total_reviews": 0,
            "average_score": 0,
            "best_score": 0,
            "worst_score": 0,
            "frontend": {},
            "backend": {},
            "database": {}
        }

    total_score = sum(
        review["score"]["overall_score"]
        for review in reviews
    )

    best_score = max(
        review["score"]["overall_score"]
        for review in reviews
    )

    worst_score = min(
        review["score"]["overall_score"]
        for review in reviews
    )

    frontend = {}
    backend = {}
    database = {}

    for review in reviews:

        technologies = review.get("technologies", {})

        fe = technologies.get("frontend") or "Unknown"
        be = technologies.get("backend") or "Unknown"
        db = technologies.get("database") or "Unknown"

        frontend[fe] = frontend.get(fe, 0) + 1
        backend[be] = backend.get(be, 0) + 1
        database[db] = database.get(db, 0) + 1

    return {
        "total_reviews": len(reviews),
        "average_score": round(total_score / len(reviews), 2),
        "best_score": best_score,
        "worst_score": worst_score,
        "frontend": frontend,
        "backend": backend,
        "database": database
    }

@app.post("/analyze-github")
def analyze_github(request: GithubRequest):
    pass