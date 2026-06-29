class AIReviewParser:

    def parse(self, review):

        sections = {}

        current = None

        for line in review.splitlines():

            if line.startswith("## "):
                current = line.replace("## ", "").strip()
                sections[current] = []

            elif current:
                sections[current].append(line)

        for key in sections:
            sections[key] = "\n".join(sections[key]).strip()

        return sections