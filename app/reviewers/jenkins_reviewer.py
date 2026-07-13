from app.reviewers.base_reviewer import BaseReviewer
from app.services.llm_service import LLMService


class JenkinsReviewer(BaseReviewer):

    def __init__(self):

        self.llm = LLMService()

    def review(self, content: str):

        prompt = f"""
You are a Senior DevOps Engineer.

Review this Jenkinsfile.

Provide

1. Score

2. Security

3. Problems

4. Best Practices

5. Optimized Pipeline

Return Markdown.

Jenkinsfile

{content}
"""

        return self.llm.ask(prompt)
