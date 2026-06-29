COMPLEXITY_LIMITS = {
    "if": 6,
    "loop": 4,
    "return": 5
}


class ComplexityDetector:

    def __init__(self, project_files):
        self.project_files = project_files

    def detect(self):

        issues = []

        for project_file in self.project_files:

            path = project_file["path"]
            content = project_file["content"].lower()

            if_count = content.count("if ")
            loop_count = (
                content.count("for ")
                + content.count("while ")
            )
            return_count = content.count("return")

            if (
                if_count > COMPLEXITY_LIMITS["if"]
                or loop_count > COMPLEXITY_LIMITS["loop"]
                or return_count > COMPLEXITY_LIMITS["return"]
            ):

                issues.append({
                    "file": path,
                    "issue": "High Code Complexity",
                    "if_count": if_count,
                    "loop_count": loop_count,
                    "return_count": return_count
                })

        return issues