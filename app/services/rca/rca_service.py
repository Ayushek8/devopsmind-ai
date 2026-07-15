import json

from app.prompts.rca_prompt import RCA_PROMPT
from app.services.llm_service import LLMService


class RCAService:

    def __init__(self):

        self.llm = LLMService()

    # ----------------------------------------

    def analyze(self, logs: str):

        prompt = RCA_PROMPT.replace(
    "{{LOGS}}",
    logs
     )

        response = self.llm.ask(
            prompt
        )

        try:

            return json.loads(response)

        except Exception:

            return {

                "title": "Unknown Failure",

                "severity": "Medium",

                "root_cause": "Unable to parse LLM response.",

                "summary": response,

                "fix": "Review deployment logs manually.",

                "commands": [],

                "confidence": 10

            }