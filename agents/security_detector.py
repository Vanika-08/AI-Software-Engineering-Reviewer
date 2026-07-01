import re


class SecurityDetector:

    def __init__(self, project_files):
        self.project_files = project_files

    def detect(self):

        issues = []

        patterns = [

            # ----------------------------
            # Hardcoded Secrets
            # ----------------------------

            (r'api[_-]?key\s*[:=]\s*["\'][^"\']+["\']',
             "HIGH",
             "Hardcoded API Key"),

            (r'secret\s*[:=]\s*["\'][^"\']+["\']',
             "HIGH",
             "Hardcoded Secret"),

            (r'password\s*[:=]\s*["\'][^"\']+["\']',
             "HIGH",
             "Hardcoded Password"),

            (r'token\s*[:=]\s*["\'][^"\']+["\']',
             "MEDIUM",
             "Hardcoded Token"),

            # ----------------------------
            # Cloud/API Keys
            # ----------------------------

            (r'AKIA[0-9A-Z]{16}',
             "CRITICAL",
             "AWS Access Key"),

            (r'ghp_[A-Za-z0-9]{36}',
             "CRITICAL",
             "GitHub Personal Access Token"),

            (r'AIza[0-9A-Za-z\-_]{35}',
             "HIGH",
             "Google API Key"),

            (r'sk-[A-Za-z0-9]{20,}',
             "HIGH",
             "OpenAI API Key"),

            (r'-----BEGIN PRIVATE KEY-----',
             "CRITICAL",
             "Private Key Found"),

            # ----------------------------
            # Dangerous Functions
            # ----------------------------

            (r'\beval\s*\(',
             "HIGH",
             "Use of eval()"),

            (r'\bexec\s*\(',
             "HIGH",
             "Use of exec()"),

            (r'new\s+Function\s*\(',
             "HIGH",
             "Use of new Function()"),

            (r'pickle\.loads',
             "HIGH",
             "Unsafe pickle.loads()"),

            (r'subprocess\..*shell\s*=\s*True',
             "HIGH",
             "subprocess(shell=True) detected"),

            (r'Runtime\.getRuntime\(\)\.exec',
             "HIGH",
             "Runtime.exec() detected"),

            (r'child_process\.exec',
             "HIGH",
             "child_process.exec() detected"),

            # ----------------------------
            # XSS
            # ----------------------------

            (r'innerHTML\s*=',
             "MEDIUM",
             "innerHTML assignment"),

            (r'document\.write\s*\(',
             "MEDIUM",
             "document.write()"),

            # ----------------------------
            # CORS
            # ----------------------------

            (r'Access-Control-Allow-Origin.*\*',
             "MEDIUM",
             "Wildcard CORS"),

        ]

        for project_file in self.project_files:

            path = project_file["path"]
            content = project_file["content"]

            for regex, severity, message in patterns:

                if re.search(regex, content, re.IGNORECASE):

                    issues.append({

                        "file": path,
                        "severity": severity,
                        "issue": message

                    })

        return issues