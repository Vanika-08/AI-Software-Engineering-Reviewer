class ScoreCalculator:

    def calculate(
        self,
        quality,
        security,
        performance,
        complexity,
        duplicate_code,
        dead_code,
        naming,
        best_practices,
        architecture
    ):

        score = 100

        # Code Quality (Maximum penalty = 20)
        score -= min(len(quality), 10) * 2

        # Security (Maximum penalty = 35)
        score -= min(len(security), 7) * 5

        # Performance (Maximum penalty = 15)
        score -= min(len(performance), 5) * 3

        # Complexity (Maximum penalty = 15)
        score -= min(len(complexity), 5) * 3

        # Duplicate Code (Maximum penalty = 10)
        score -= min(len(duplicate_code), 5) * 2

        # Dead Code (Maximum penalty = 10)
        score -= min(len(dead_code), 5) * 2

        # Naming Convention (Maximum penalty = 10)
        score -= min(len(naming), 5) * 2

        # Best Practices (Maximum penalty depends on checks)
        for value in best_practices.values():
            if not value:
                score -= 2

        # Architecture (Maximum penalty depends on checks)
        for value in architecture.values():
            if not value:
                score -= 2

        score = max(score, 0)

        return {
            "overall_score": score
        }