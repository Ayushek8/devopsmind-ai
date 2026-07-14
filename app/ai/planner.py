import json

from app.services.llm_service import LLMService
from app.schemas.execution_command import ExecutionCommand
from app.utils.json_parser import JSONParser


class Planner:

    def __init__(self):

        self.llm = LLMService()

    def plan(self, user_request: str):

        prompt = f"""
You are an AI DevOps Planner.

Convert the user's request into an execution plan.

Return ONLY valid JSON.

Never wrap the JSON inside markdown.

Never use ```json.

Never explain.

Only return JSON.

Use ONLY these actions:

- list
- create
- start
- stop
- terminate
- delete
- update
- deploy

Return exactly like this:

{{
    "domain":"aws",
    "service":"ec2",
    "action":"list",
    "parameters":{{}}
}}

User Request:

{user_request}
"""

        response = self.llm.ask(prompt)

        print("=" * 70)
        print("Planner Raw Response")
        print("=" * 70)
        print(response)

        data = JSONParser.parse(response)

        print("=" * 70)
        print("Execution Command")
        print("=" * 70)
        print(data)

        return ExecutionCommand(**data)
