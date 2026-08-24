from app.agents.github.github_agent import GitHubAgent
from app.services.llm_service import LLMService
from app.utils.json_parser import JSONParser


class IntentRouter:

    def __init__(self):

        self.github = GitHubAgent()
        self.llm = LLMService()

    def route(self, command):

        try:

            if command.domain == "github":

                return self.github.execute(command)

            # Behave like ChatGPT for general chat or other unsupported domains
            question = command.parameters.get("question", "")
            if not question:
                question = f"Help with command: {command.domain} {command.service} {command.action}"

            prompt = f"""
You are DevOpsMind, a highly intelligent AI SRE and DevOps expert.
Your goal is to answer the user's question or help them resolve their issue.
Answer in the same language as the user's question. Use clear, helpful formatting.

Return ONLY a JSON object matching this schema:
{{
    "answer": "<your helpful answer here>"
}}

User Question: {question}
"""
            response = self.llm.ask(prompt)
            parsed = JSONParser.parse(response)
            return parsed.get("answer", response)

        except Exception as e:

            return {

                "type": "error",

                "response": str(e)

            }
