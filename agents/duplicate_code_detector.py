import hashlib


class DuplicateCodeDetector:

    def __init__(self, project_files):
        self.project_files = project_files

    def detect(self):

        issues = []

        seen_hashes = {}

        for project_file in self.project_files:

            content = project_file["content"].strip()

            # Ignore very small files
            if len(content) < 300:
                continue

            file_hash = hashlib.sha256(
                content.encode("utf-8")
            ).hexdigest()

            if file_hash in seen_hashes:

                issues.append({
                    "file1": seen_hashes[file_hash],
                    "file2": project_file["path"],
                    "similarity": 100,
                    "issue": "Duplicate Code Detected"
                })

            else:

                seen_hashes[file_hash] = project_file["path"]

        return issues