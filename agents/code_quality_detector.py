import re


class CodeQualityDetector:

    def __init__(self, project_files):
        self.project_files = project_files

    def detect(self):

        issues = []

        for project_file in self.project_files:

            path = project_file["path"]
            content = project_file["content"]
            lower = content.lower()

            # ------------------------------
            # JavaScript / TypeScript
            # ------------------------------

            if path.endswith((".js", ".jsx", ".ts", ".tsx")):

                if "console.log(" in content:
                    issues.append({
                        "file": path,
                        "issue": "Console Log Found"
                    })

                if "debugger;" in content:
                    issues.append({
                        "file": path,
                        "issue": "Debugger Statement Found"
                    })

                if re.search(r"\bvar\s+", content):
                    issues.append({
                        "file": path,
                        "issue": "Use let/const instead of var"
                    })

                if "eval(" in content:
                    issues.append({
                        "file": path,
                        "issue": "Avoid eval()"
                    })

                if "document.write(" in content:
                    issues.append({
                        "file": path,
                        "issue": "Avoid document.write()"
                    })

            # ------------------------------
            # Python
            # ------------------------------

            if path.endswith(".py"):

                if "print(" in content:
                    issues.append({
                        "file": path,
                        "issue": "Debug print() Found"
                    })

                if "eval(" in content:
                    issues.append({
                        "file": path,
                        "issue": "Avoid eval()"
                    })

            # ------------------------------
            # Java
            # ------------------------------

            if path.endswith(".java"):

                if "system.out.println" in lower:
                    issues.append({
                        "file": path,
                        "issue": "Debug Print Statement"
                    })

            # ------------------------------
            # Generic
            # ------------------------------

            if "todo" in lower:
                issues.append({
                    "file": path,
                    "issue": "TODO Found"
                })

            if "fixme" in lower:
                issues.append({
                    "file": path,
                    "issue": "FIXME Found"
                })

            # ------------------------------
            # Long File
            # ------------------------------

            line_count = len(content.splitlines())

            if line_count > 500:

                issues.append({
                    "file": path,
                    "issue": f"Large File ({line_count} lines)"
                })

            # ------------------------------
            # Long Function (basic)
            # ------------------------------

            functions = re.findall(
                r"(function\s+\w+.*?\{)|"
                r"(def\s+\w+\(.*?\):)|"
                r"(public\s+.*?\{)|"
                r"(private\s+.*?\{)",
                content,
                re.DOTALL
            )

            if len(functions) > 25:

                issues.append({
                    "file": path,
                    "issue": "Too Many Functions in File"
                })

        return issues