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

        # Maximum penalty = 20
        score -= min(len(quality), 10) * 2

        # Maximum penalty = 35
        score -= min(len(security), 7) * 5

        # Maximum penalty = 15
        score -= min(len(performance), 5) * 3

        # Best Practices
        for value in best_practices.values():
            if not value:
                score -= 2

        # Architecture
        for value in architecture.values():
            if not value:
                score -= 2

        score = max(score, 0)

        return {
            "overall_score": score
        }