TECH_RULES = {

    "package.json": {
        "react": "React",
        "next": "Next.js",
        "vue": "Vue",
        "angular": "Angular",
        "express": "Express.js",
        "mongoose": "MongoDB"
    },

    "requirements.txt": {
        "django": "Django",
        "flask": "Flask",
        "fastapi": "FastAPI"
    },

    "pom.xml": {
        "spring-boot": "Spring Boot"
    }
}

FRONTEND = {
    "React",
    "Next.js",
    "Vue",
    "Angular"
}

BACKEND = {
    "Express.js",
    "Spring Boot",
    "FastAPI",
    "Django",
    "Flask"
}

DATABASE = {
    "MongoDB"
}

class TechnologyDetector:

    def __init__(self, project_files):
        self.project_files = project_files

    
    def detect(self):

        technologies = {
        "frontend": None,
        "backend": None,
        "database": None
}

        for project_file in self.project_files:

            filename = project_file["path"].split("/")[-1]

            if filename not in TECH_RULES:
                continue

            content = project_file["content"].lower()

            rules = TECH_RULES[filename]
            for keyword, technology in rules.items():

                if keyword in content:

                    if technology in FRONTEND:
                        technologies["frontend"] = technology

                    elif technology in BACKEND:
                        technologies["backend"] = technology

                    elif technology in DATABASE:
                        technologies["database"] = technology

        return technologies