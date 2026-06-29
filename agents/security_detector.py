import re

SECURITY_PATTERNS = [
    (
        re.compile(r'(api[_-]?key)\s*[:=]\s*["\'][^"\']+["\']', re.IGNORECASE),
        "HIGH",
        "Hardcoded API Key"
    ),
    (
        re.compile(r'(secret)\s*[:=]\s*["\'][^"\']+["\']', re.IGNORECASE),
        "HIGH",
        "Hardcoded Secret"
    ),
    (
        re.compile(r'(password)\s*[:=]\s*["\'][^"\']+["\']', re.IGNORECASE),
        "HIGH",
        "Hardcoded Password"
    ),
    (
        re.compile(r'(token)\s*[:=]\s*["\'][^"\']+["\']', re.IGNORECASE),
        "MEDIUM",
        "Hardcoded Token"
    ),
    (
        re.compile(r'-----BEGIN\s+PRIVATE\s+KEY-----'),
        "CRITICAL",
        "Private Key Found"
    ),
    (
        re.compile(r'aws_access_key_id\s*[:=]\s*["\'][^"\']+["\']', re.IGNORECASE),
        "CRITICAL",
        "AWS Access Key Found"
    ),
    (
        re.compile(r'aws_secret_access_key\s*[:=]\s*["\'][^"\']+["\']', re.IGNORECASE),
        "CRITICAL",
        "AWS Secret Access Key Found"
    )
]


class SecurityDetector:

    def __init__(self, project_files):
        self.project_files = project_files

    def detect(self):

        issues = []

        for project_file in self.project_files:

            path = project_file["path"]
            content = project_file["content"]

            for pattern, severity, message in SECURITY_PATTERNS:

                if pattern.search(content):

                    issues.append({
                        "file": path,
                        "severity": severity,
                        "issue": message
                    })

        return issues