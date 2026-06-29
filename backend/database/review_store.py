import json
from pathlib import Path

DB_FILE = Path(__file__).parent / "reviews.json"


class ReviewStore:

    def save(self, report):

        reviews = []

        if DB_FILE.exists():
            with open(DB_FILE, "r") as f:
                reviews = json.load(f)

        reviews.append(report)

        with open(DB_FILE, "w") as f:
            json.dump(reviews, f, indent=4)

    def get_all(self):

        if not DB_FILE.exists():
            return []

        with open(DB_FILE, "r") as f:
            return json.load(f)