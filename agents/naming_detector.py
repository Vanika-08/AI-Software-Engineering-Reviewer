import re


class NamingDetector:

    def __init__(self, project_files):
        self.project_files = project_files

    def detect(self):

        issues = []

        function_pattern = re.compile(
            r"def\s+([A-Za-z0-9_]+)|function\s+([A-Za-z0-9_]+)"
        )

        class_pattern = re.compile(
            r"class\s+([A-Za-z0-9_]+)"
        )

        for project_file in self.project_files:

            path = project_file["path"]
            content = project_file["content"]

            # Functions
            for match in function_pattern.finditer(content):

                name = match.group(1) or match.group(2)

                if (
                    len(name) <= 2
                    or "_" in name
                    or name.isupper()
                ):

                    issues.append({
                        "file": path,
                        "type": "Function",
                        "name": name,
                        "issue": "Poor Function Naming"
                    })

            # Classes
            for match in class_pattern.finditer(content):

                name = match.group(1)

                if not name[:1].isupper():

                    issues.append({
                        "file": path,
                        "type": "Class",
                        "name": name,
                        "issue": "Class should use PascalCase"
                    })

        return issues