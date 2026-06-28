from pathlib import Path


class BestPracticesDetector:

    def __init__(self, project_path):
        self.project_path = Path(project_path)

    def detect(self):

        result = {
            "readme": False,
            "gitignore": False,
            "dockerfile": False,
            "env_example": False,
            "eslint": False,
            "prettier": False,
            "package_lock": False,
            "tsconfig": False
        }

        for file in self.project_path.rglob("*"):

            if not file.is_file():
                continue

            name = file.name.lower()

            if name == "readme.md":
                result["readme"] = True

            elif name == ".gitignore":
                result["gitignore"] = True

            elif name == "dockerfile":
                result["dockerfile"] = True

            elif name == ".env.example":
                result["env_example"] = True

            elif name == ".eslintrc" or name.startswith(".eslintrc"):
                result["eslint"] = True

            elif "prettier" in name:
                result["prettier"] = True

            elif name == "package-lock.json":
                result["package_lock"] = True

            elif name == "tsconfig.json":
                result["tsconfig"] = True

        return result