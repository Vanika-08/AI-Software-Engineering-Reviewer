from difflib import SequenceMatcher


class DuplicateCodeDetector:

    def __init__(self, project_files):
        self.project_files = project_files

    def detect(self):

        issues = []

        for i in range(len(self.project_files)):

            file1 = self.project_files[i]

            for j in range(i + 1, len(self.project_files)):

                file2 = self.project_files[j]

                similarity = SequenceMatcher(
                    None,
                    file1["content"],
                    file2["content"]
                ).ratio()

                if (
                    len(file1["content"]) > 300
                    and len(file2["content"]) > 300
                    and similarity >= 0.90
                ):

                    issues.append({
                        "file1": file1["path"],
                        "file2": file2["path"],
                        "similarity": round(similarity * 100, 2),
                        "issue": "Duplicate Code Detected"
                    })

        return issues