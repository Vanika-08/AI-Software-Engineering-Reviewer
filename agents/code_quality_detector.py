QUALITY_RULES = {
    "console.log": "Console Log Found",
    "todo": "TODO Found",
    "fixme": "FIXME Found",
    "debugger": "Debugger Statement",
    "eval(": "Use of eval()",
    "var ": "Use let/const instead of var"
}


class CodeQualityDetector:

    def __init__(self, project_files):
        self.project_files = project_files

    def detect(self):

        issues = []

        for project_file in self.project_files:

            path = project_file["path"]
            content = project_file["content"].lower()

            for keyword, message in QUALITY_RULES.items():

                count = content.count(keyword)

                if count > 0:

                    issues.append({
                        "file": path,
                        "issue": message,
                        "count": count
                    })

        return issues  