from app.services.llm_service import LLMService


class FileDetector:

    def __init__(self):
        self.llm = LLMService()

    def detect(self, content: str) -> str:

        prompt = f"""
You are a DevOps file classifier.

Determine what type of DevOps file this is.

Supported file types:

- jenkins
- docker
- kubernetes
- terraform
- github-actions
- ansible
- bash
- python
- unknown

Return ONLY ONE WORD.

File Content:

{content}
"""

        response = self.llm.ask(prompt)

        return response.strip().lower()
