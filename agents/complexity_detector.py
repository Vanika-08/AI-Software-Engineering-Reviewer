import re


class ComplexityDetector:

    def __init__(self, project_files):
        self.project_files = project_files

    def detect(self):

        issues = []

        for project_file in self.project_files:

            path = project_file["path"]
            content = project_file["content"]

            # ----------------------------
            # Cyclomatic Complexity (Heuristic)
            # ----------------------------

            complexity = 1

            keywords = [
                "if ",
                "else if",
                "elif ",
                "for ",
                "while ",
                "case ",
                "catch",
                "except",
                "&&",
                "||",
                "?",
            ]

            lower = content.lower()

            for keyword in keywords:
                complexity += lower.count(keyword)

            if complexity > 15:

                issues.append({
                    "file": path,
                    "issue": "High Cyclomatic Complexity",
                    "complexity": complexity
                })

            # ----------------------------
            # Nesting Depth
            # ----------------------------

            max_depth = 0
            current_depth = 0

            for line in content.splitlines():

                stripped = line.strip()

                if stripped.endswith("{"):
                    current_depth += 1
                    max_depth = max(max_depth, current_depth)

                if stripped.startswith("}"):
                    current_depth = max(current_depth - 1, 0)

            if max_depth > 5:

                issues.append({
                    "file": path,
                    "issue": "Deep Nesting Detected",
                    "depth": max_depth
                })

            # ----------------------------
            # Long Functions (Heuristic)
            # ----------------------------

            lines = content.splitlines()

            function_lines = 0
            inside_function = False

            for line in lines:

                if re.search(
                    r"(function\s+\w+)|(def\s+\w+)|(public\s+)|(private\s+)|(protected\s+)",
                    line
                ):
                    inside_function = True
                    function_lines = 0

                if inside_function:
                    function_lines += 1

                if "}" in line or line.strip() == "":
                    if function_lines > 80:

                        issues.append({
                            "file": path,
                            "issue": "Long Function",
                            "lines": function_lines
                        })

                    inside_function = False

            # ----------------------------
            # Too Many Parameters
            # ----------------------------

            parameter_matches = re.findall(
                r"\((.*?)\)",
                content
            )

            for params in parameter_matches:

                if len(params.split(",")) > 6:

                    issues.append({
                        "file": path,
                        "issue": "Too Many Parameters"
                    })

                    break

            # ----------------------------
            # Large File
            # ----------------------------

            line_count = len(lines)

            if line_count > 1000:

                issues.append({
                    "file": path,
                    "issue": "Very Large Source File",
                    "lines": line_count
                })

        return issues