from pathlib import Path


class StructureDetector:

    def __init__(self, project_path):
        self.project_path = Path(project_path)

    def detect(self):
        folders = set()

        for folder in self.project_path.rglob("*"):

            if folder.is_dir():
                folders.add(folder.relative_to(self.project_path))

        result = {
            "src": False,
            "components": False,
            "pages": False,
            "services": False,
            "utils": False,
            "hooks": False,
            "assets": False
        }

        for folder in folders:

            parts = Path(folder).parts

            if "src" in parts:
                result["src"] = True

            if "components" in parts:
                result["components"] = True

            if "pages" in parts:
                result["pages"] = True

            if "services" in parts:
                result["services"] = True

            if "utils" in parts:
                result["utils"] = True

            if "hooks" in parts:
                result["hooks"] = True

            if "assets" in parts:
                result["assets"] = True

        return result