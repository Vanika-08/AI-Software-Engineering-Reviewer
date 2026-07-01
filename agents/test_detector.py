TEST_FRAMEWORKS = {
    "jest": "Jest",
    "pytest": "PyTest",
    "junit": "JUnit",
    "cypress": "Cypress",
    "playwright": "Playwright",
    "mocha": "Mocha",
    "vitest": "Vitest",
    "karma": "Karma",
    "testing-library": "Testing Library"
}


class TestDetector:

    def __init__(self, project_files):
        self.project_files = project_files

    def detect(self):

        detected = set()

        for project_file in self.project_files:

            path = project_file["path"].lower()
            content = project_file["content"].lower()

            for keyword, framework in TEST_FRAMEWORKS.items():

                if keyword in path or keyword in content:
                    detected.add(framework)

        if not detected:

            return [{
                "framework": "None",
                "issue": "No Testing Framework Detected"
            }]

        return [
            {
                "framework": framework,
                "issue": "Testing Framework Detected"
            }
            for framework in sorted(detected)
        ]