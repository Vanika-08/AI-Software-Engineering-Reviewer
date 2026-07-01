import re


class PerformanceDetector:

    def __init__(self, project_files):
        self.project_files = project_files

    def detect(self):

        issues = []

        for project_file in self.project_files:

            path = project_file["path"]
            content = project_file["content"]
            lower = content.lower()

            # ----------------------------
            # JavaScript / TypeScript
            # ----------------------------

            if path.endswith((".js", ".jsx", ".ts", ".tsx")):

                if "setinterval(" in lower:
                    issues.append({
                        "file": path,
                        "issue": "Avoid setInterval() when possible"
                    })

                if "innerhtml" in lower:
                    issues.append({
                        "file": path,
                        "issue": "Avoid excessive innerHTML usage"
                    })

                if "document.write(" in lower:
                    issues.append({
                        "file": path,
                        "issue": "document.write() hurts performance"
                    })

                if "console.time(" in lower:
                    issues.append({
                        "file": path,
                        "issue": "Remove console.time() before production"
                    })

                if "console.log(" in lower:
                    issues.append({
                        "file": path,
                        "issue": "Remove console.log() in production"
                    })

            # ----------------------------
            # Node.js
            # ----------------------------

            if "readfilesync(" in lower:
                issues.append({
                    "file": path,
                    "issue": "Use asynchronous file reading"
                })

            if "writefilesync(" in lower:
                issues.append({
                    "file": path,
                    "issue": "Use asynchronous file writing"
                })

            # ----------------------------
            # Python
            # ----------------------------

            if path.endswith(".py"):

                if "time.sleep(" in lower:
                    issues.append({
                        "file": path,
                        "issue": "Blocking sleep() detected"
                    })

            # ----------------------------
            # React
            # ----------------------------

            if path.endswith((".jsx", ".tsx")):

                if "usestate(" in lower and "usememo(" not in lower:
                    issues.append({
                        "file": path,
                        "issue": "Consider useMemo() for expensive calculations"
                    })

            # ----------------------------
            # Large File
            # ----------------------------

            line_count = len(content.splitlines())

            if line_count > 800:
                issues.append({
                    "file": path,
                    "issue": "Very large file may affect maintainability"
                })

            # ----------------------------
            # Long Lines
            # ----------------------------

            for line in content.splitlines():

                if len(line) > 180:

                    issues.append({
                        "file": path,
                        "issue": "Very long line detected"
                    })

                    break

            # ----------------------------
            # Nested Loops (basic heuristic)
            # ----------------------------

            nested = re.findall(
                r"for\s+.*?\n(?:.*\n){0,8}.*for\s+",
                content,
                re.MULTILINE
            )

            if nested:
                issues.append({
                    "file": path,
                    "issue": "Possible nested loop detected"
                })

        return issues