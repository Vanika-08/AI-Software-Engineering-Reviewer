from pathlib import Path
import zipfile

class ProjectReader:
    def __init__(self, upload_id):
        self.upload_id = upload_id
        self.upload_path = Path("uploads") / upload_id

    def extract_zip(self):

        zip_file = self.upload_path / "original.zip"
        extract_folder = self.upload_path / "extracted"
        extract_folder.mkdir(exist_ok=True)
        with zipfile.ZipFile(zip_file, "r") as zip_ref:
            zip_ref.extractall(extract_folder)

        print("Extracted to:", extract_folder)

        for item in extract_folder.rglob("*"):
            print(item)

        return extract_folder
    
    def read_project_files(self):

        extracted_folder = self.upload_path / "extracted"

        project_files = []

        ignore_folders = {
            "node_modules",
            ".git",
            "dist",
            "build",
            "__pycache__",
            ".next",
            ".idea",
            ".vscode"
        }

        allowed_extensions = {
            ".py",
            ".js",
            ".jsx",
            ".ts",
            ".tsx",
            ".java",
            ".html",
            ".css",
            ".scss",
            ".json",
            ".md",
            ".xml",
            ".yml",
            ".yaml",
            ".properties"
        }

        for file in extracted_folder.rglob("*"):
            if not file.is_file():
                continue

            if any(folder in file.parts for folder in ignore_folders):
                continue

            if file.suffix.lower() not in allowed_extensions:
                continue

            try:
                content = file.read_text(encoding="utf-8")

                print(file.relative_to(extracted_folder))

                project_files.append({
                    "path": str(file.relative_to(extracted_folder)),
                    "content": content
                })

            except Exception:
                continue

        return project_files