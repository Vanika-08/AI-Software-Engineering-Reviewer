import os

PACKAGE_RULES = {
    "package.json": {
        "react": "React",
        "next": "Next.js",
        "vue": "Vue.js",
        "@angular/core": "Angular",
        "express": "Express.js",
        "nestjs": "NestJS",
        "koa": "Koa",
        "hapi": "Hapi",
        "mongodb": "MongoDB",
        "mongoose": "MongoDB",
        "mysql": "MySQL",
        "mysql2": "MySQL",
        "pg": "PostgreSQL",
        "sqlite": "SQLite",
        "firebase": "Firebase",
        "redis": "Redis",
        "tailwindcss": "Tailwind CSS",
        "bootstrap": "Bootstrap",
        "jquery": "jQuery",
        "@mui/material": "Material UI",
        "antd": "Ant Design"
    },

    "requirements.txt": {
        "django": "Django",
        "flask": "Flask",
        "fastapi": "FastAPI",
        "sqlalchemy": "SQLAlchemy",
        "pymongo": "MongoDB",
        "psycopg2": "PostgreSQL",
        "mysqlclient": "MySQL",
        "firebase-admin": "Firebase",
        "redis": "Redis"
    },

    "pom.xml": {
        "spring-boot": "Spring Boot",
        "spring-data-jpa": "Spring Data JPA",
        "mysql": "MySQL",
        "postgresql": "PostgreSQL",
        "mongodb": "MongoDB"
    },

    "composer.json": {
        "laravel": "Laravel"
    }
}


class TechnologyDetector:

    def __init__(self, project_files):
        self.project_files = project_files

    def detect(self):

        frontend = set()
        backend = set()
        database = set()

        html_found = False
        css_found = False
        js_found = False

        for project_file in self.project_files:

            path = project_file["path"].lower()
            filename = os.path.basename(path)
            content = project_file["content"].lower()

            # ----------------------------
            # Detect by file extension
            # ----------------------------

            if path.endswith(".html"):
                html_found = True

            if path.endswith(".css") or path.endswith(".scss"):
                css_found = True

            if path.endswith((".js", ".jsx", ".ts", ".tsx")):
                js_found = True

            # ----------------------------
            # Detect from dependency files
            # ----------------------------

            if filename in PACKAGE_RULES:

                for keyword, tech in PACKAGE_RULES[filename].items():

                    if keyword not in content:
                        continue

                    if tech in {
                        "React",
                        "Next.js",
                        "Vue.js",
                        "Angular",
                        "Tailwind CSS",
                        "Bootstrap",
                        "Material UI",
                        "Ant Design",
                        "jQuery"
                    }:
                        frontend.add(tech)

                    elif tech in {
                        "Express.js",
                        "NestJS",
                        "Koa",
                        "Hapi",
                        "Spring Boot",
                        "Spring Data JPA",
                        "Django",
                        "Flask",
                        "FastAPI",
                        "Laravel"
                    }:
                        backend.add(tech)

                    elif tech in {
                        "MongoDB",
                        "MySQL",
                        "PostgreSQL",
                        "SQLite",
                        "Firebase",
                        "Redis"
                    }:
                        database.add(tech)

        # Generic frontend detection

        if html_found:
            frontend.add("HTML")

        if css_found:
            frontend.add("CSS")

        if js_found:
            frontend.add("JavaScript")

        return {
            "frontend": sorted(frontend) if frontend else [],
            "backend": sorted(backend) if backend else [],
            "database": sorted(database) if database else []
        }