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

Generate your response ONLY in the following Markdown format.

## Overall Summary
Write a short summary of the project in 3-5 sentences.

## Strengths
- Bullet point
- Bullet point
- Bullet point

## Weaknesses
- Bullet point
- Bullet point
- Bullet point

## Security Improvements
- Bullet point
- Bullet point

## Performance Improvements
- Bullet point
- Bullet point

## Code Quality Suggestions
- Bullet point
- Bullet point

## Final Verdict
Write a concise overall verdict in 2-3 sentences.

## Final Score
Return ONLY a number between 0 and 100.
"""