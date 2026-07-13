from app.services.llm_service import LLMService


class ResponseFormatter:

    def __init__(self):

        self.llm = LLMService()

    def format(self, command: str, result):

        prompt = f"""
You are an AI DevOps Engineer.

The user executed this command:

{command}

The AWS response is:

{result}

Explain the result in professional, human-friendly language.

Keep it concise.

Mention important observations.

"""

        return self.llm.ask(prompt)
