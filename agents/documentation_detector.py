import re


class DocumentationDetector:

    def __init__(self, project_files):
        self.project_files = project_files

    def detect(self):

        issues = []

        comment_patterns = [
            "//",
            "#",
            "/*",
            '"""',
            "'''"
        ]

        for project_file in self.project_files:

            path = project_file["path"]
            content = project_file["content"]

            lines = content.splitlines()

            if len(lines) < 20:
                continue

            comment_count = 0

            for line in lines:

                stripped = line.strip()

                if any(
                    stripped.startswith(pattern)
                    for pattern in comment_patterns
                ):
                    comment_count += 1

            ratio = comment_count / len(lines)

            if ratio < 0.03:

                issues.append({
                    "file": path,
                    "issue": "Very Low Documentation",
                    "comments": comment_count,
                    "lines": len(lines)
                })

        return issues