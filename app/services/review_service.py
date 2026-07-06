from app.services.llm_service import LLMService


class ReviewService:

    def __init__(self):
        self.llm = LLMService()

    def review_jenkinsfile(self, content: str):

        prompt = f"""
You are a Senior DevOps Engineer.

Review the following Jenkinsfile.

Give:

1. Overall Score out of 100

2. Good Practices

3. Problems

4. Security Issues

5. Suggested Improvements

Return the response in Markdown.

Jenkinsfile:

{content}
"""

        return self.llm.ask(prompt)