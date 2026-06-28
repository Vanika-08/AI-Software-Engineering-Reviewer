class ScoreCalculator:

    def calculate(
        self,
        quality,
        security,
        performance,
        best_practices,
        architecture
    ):

        score = 100

        score -= len(quality) * 2
        score -= len(security) * 5
        score -= len(performance) * 3

        for value in best_practices.values():
            if not value:
                score -= 2

        for value in architecture.values():
            if not value:
                score -= 2

        score = max(score, 0)

        return {
            "overall_score": score
        }