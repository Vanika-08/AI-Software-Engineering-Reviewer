class PromptBuilder:

    def build(self, report, context):

        return f"""
You are a Senior Software Engineer.

Review this project.

Technologies:
{report["technologies"]}

Architecture:
{report["architecture"]}

Security:
{report["security"]}

Quality:
{report["quality"]}

Performance:
{report["performance"]}

Best Practices:
{report["best_practices"]}

Relevant Code:
{context}

Generate a professional review containing:

1. Overall Summary
2. Strengths
3. Weaknesses
4. Security Improvements
5. Performance Improvements
6. Code Quality Suggestions
7. Final Score out of 100
"""