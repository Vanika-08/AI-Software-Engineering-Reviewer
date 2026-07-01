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

        return extract_folder

    def read_project_files(self):

        extracted_folder = self.upload_path / "extracted"

        project_files = []

        ignore_folders = {

            # Git
            ".git",

            # Node
            "node_modules",

            # Python
            "venv",
            ".venv",
            "env",
            "__pycache__",
            ".pytest_cache",
            ".mypy_cache",
            ".tox",

            # React / Next
            ".next",
            "dist",
            "build",

            # IDE
            ".idea",
            ".vscode",

            # Java
            "target",
            ".gradle",

            # Flutter
            ".dart_tool",

            # Android
            ".android",

            # iOS
            "Pods",

            # Coverage
            "coverage"
        }

        ignore_files = {

            # Node
            "package-lock.json",
            "yarn.lock",
            "pnpm-lock.yaml",
            "bun.lockb",

            # Python
            "poetry.lock",
            "Pipfile.lock",

            # Misc
            ".DS_Store",
            "Thumbs.db"
        }

        allowed_extensions = {

            # Python
            ".py",

            # JavaScript
            ".js",
            ".jsx",
            ".ts",
            ".tsx",

            # Java
            ".java",
            ".kt",

            # C/C++
            ".c",
            ".cpp",
            ".h",
            ".hpp",

            # C#
            ".cs",

            # PHP
            ".php",

            # Go
            ".go",

            # Rust
            ".rs",

            # Ruby
            ".rb",

            # Swift
            ".swift",

            # Frontend
            ".html",
            ".css",
            ".scss",

            # Config
            ".json",
            ".xml",
            ".yml",
            ".yaml",
            ".properties",

            # Database
            ".sql",

            # Documentation
            ".md"
        }

        for file in extracted_folder.rglob("*"):

            if not file.is_file():
                continue

            if any(folder in file.parts for folder in ignore_folders):
                continue

            if file.name in ignore_files:
                continue

            if file.suffix.lower() not in allowed_extensions:
                continue

            try:

                content = file.read_text(
                    encoding="utf-8",
                    errors="ignore"
                )

                project_files.append({

                    "path": str(file.relative_to(extracted_folder)),
                    "content": content

                })

            except Exception:

                continue

        print(f"Loaded {len(project_files)} source files")

        return project_files