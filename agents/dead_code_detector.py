EMPTY_FUNCTIONS = [
    "pass",
    "{}",
    "return",
    "return None"
]


class DeadCodeDetector:

    def __init__(self, project_files):
        self.project_files = project_files

    def detect(self):

        issues = []

        for project_file in self.project_files:

            path = project_file["path"]
            content = project_file["content"]

            stripped = content.strip()

            # Empty file
            if len(stripped) == 0:

                issues.append({
                    "file": path,
                    "issue": "Empty File"
                })

                continue

            # Empty Python function
            if "pass" in content:

                issues.append({
                    "file": path,
                    "issue": "Possible Empty Function/Class"
                })

            # Empty JS/TS function
            if (
                "function" in content
                and "{}" in content.replace(" ", "")
            ):

                issues.append({
                    "file": path,
                    "issue": "Empty Function"
                })

        return issues