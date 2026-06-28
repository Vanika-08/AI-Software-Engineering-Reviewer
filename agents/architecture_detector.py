from pathlib import Path


class ArchitectureDetector:

    def __init__(self, project_path):
        self.project_path = Path(project_path)

    def detect(self):

        result = {
            "readme": False,
            "gitignore": False,
            "package_json": False,
            "src": False,
            "public": False,
            "tests": False
        }

        for file in self.project_path.rglob("*"):

            if not file.is_file():
                continue

            name = file.name.lower()

            if name == "readme.md":
                result["readme"] = True

            elif name == ".gitignore":
                result["gitignore"] = True

            elif name == "package.json":
                result["package_json"] = True

            elif "src" in file.parts:
                result["src"] = True

            elif "public" in file.parts:
                result["public"] = True

            elif "test" in name or "tests" in file.parts:
                result["tests"] = True

        return result