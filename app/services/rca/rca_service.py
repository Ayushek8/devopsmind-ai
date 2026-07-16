import json

from app.prompts.rca_prompt import RCA_PROMPT
from app.services.llm_service import LLMService
from app.utils.json_parser import JSONParser


class RCAService:

    def __init__(self):

        self.llm = LLMService()

    # --------------------------------------------------------

    def analyze(self, logs: str):

        prompt = RCA_PROMPT.replace(

            "{{LOGS}}",

            logs

        )

        response = self.llm.ask(

            prompt

        )

        print("=" * 80)
        print("LLM RAW RESPONSE")
        print("=" * 80)
        print(response)

        try:

            incident = JSONParser.parse(

                response

            )

            print("=" * 80)
            print("PARSED INCIDENT")
            print("=" * 80)
            print(incident)

            # ---------------------------------------------
            # Safety Defaults
            # ---------------------------------------------

            incident.setdefault(

                "title",

                "Unknown Failure"

            )

            incident.setdefault(

                "severity",

                "Medium"

            )

            incident.setdefault(

                "root_cause",

                "Not Available"

            )

            incident.setdefault(

                "summary",

                "No Summary Generated"

            )

            incident.setdefault(

                "fix",

                "Review deployment logs manually."

            )

            incident.setdefault(

                "commands",

                []

            )

            incident.setdefault(

                "confidence",

                50

            )

            # Convert string → list if needed

            if isinstance(

                incident["commands"],

                str

            ):

                incident["commands"] = [

                    incident["commands"]

                ]

            print("=" * 80)
            print("FINAL INCIDENT")
            print("=" * 80)
            print(incident)

            return incident

        except Exception as e:

            print("=" * 80)
            print("RCA PARSE ERROR")
            print("=" * 80)
            print(e)

            return {

                "title": "Unknown Failure",

                "severity": "Medium",

                "root_cause": "Unable to parse LLM response.",

                "summary": response,

                "fix": "Review deployment logs manually.",

                "commands": [],

                "confidence": 10

            }