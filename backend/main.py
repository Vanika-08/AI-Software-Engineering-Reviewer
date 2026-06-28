from fastapi import FastAPI, UploadFile, File
from pathlib import Path
import uuid
from datetime import datetime
import shutil
from agents.project_reader import ProjectReader
from agents.review_coordinator import ReviewCoordinator

app = FastAPI()
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

    for file in project_files:
        print(file["path"])

    print(project_files)

    coordinator = ReviewCoordinator(project_files, extract_folder)

    report = coordinator.run()

    return {
        "message": "Project uploaded successfully",
        "upload_id": upload_id,
        **report,
        "total_files": len(project_files),
        "files": project_files[:5]
    }