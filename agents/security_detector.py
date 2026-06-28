SECURITY_RULES = {
    "api_key": ("HIGH", "Hardcoded API Key"),
    "apikey": ("HIGH", "Hardcoded API Key"),
    "secret": ("HIGH", "Hardcoded Secret"),
    "password": ("HIGH", "Hardcoded Password"),
    "token": ("MEDIUM", "Hardcoded Token"),
    "private key": ("CRITICAL", "Private Key Found"),
    "aws_access_key": ("CRITICAL", "AWS Access Key Found"),
    "aws_secret_access_key": ("CRITICAL", "AWS Secret Access Key Found")
}


class SecurityDetector:

    def __init__(self, project_files):
        self.project_files = project_files

    def detect(self):

        issues = []

        for project_file in self.project_files:

            path = project_file["path"]
            content = project_file["content"].lower()

            for keyword, (severity, message) in SECURITY_RULES.items():

                if keyword in content:

                    issues.append({
                        "file": path,
                        "severity": severity,
                        "issue": message
                    })

        return issues