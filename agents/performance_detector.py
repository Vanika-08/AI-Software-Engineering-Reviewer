PERFORMANCE_RULES = {
    "console.time(": "Console Timer Found",
    "setinterval(": "setInterval Used",
    "innerhtml": "innerHTML Used",
    "readfilesync(": "Synchronous File Read",
    "writefilesync(": "Synchronous File Write"
}


class PerformanceDetector:

    def __init__(self, project_files):
        self.project_files = project_files

    def detect(self):

        issues = []

        for project_file in self.project_files:

            path = project_file["path"]
            content = project_file["content"].lower()

            for keyword, message in PERFORMANCE_RULES.items():

                if keyword in content:

                    issues.append({
                        "file": path,
                        "issue": message
                    })

        return issues