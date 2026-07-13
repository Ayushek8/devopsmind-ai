import json

from app.constants.actions import ACTION_ALIASES
from app.services.llm_service import LLMService
from app.schemas.execution_command import ExecutionCommand


class Planner:

    def __init__(self):
        self.llm = LLMService()

    def plan(self, user_request: str):

        prompt = f"""
You are an AI DevOps Planner.

Your responsibility is to convert the user's request into an execution plan.

Return ONLY valid JSON.

Use ONLY these action names:

- list
- create
- start
- stop
- terminate
- delete
- update

Never return AWS API names like:
- DescribeInstances
- RunInstances
- StopInstances
- StartInstances

Return exactly in this format:

{{
    "domain": "aws",
    "service": "ec2",
    "action": "list",
    "parameters": {{}}
}}

User Request:
{user_request}
"""

        response = self.llm.ask(prompt)

        print("=" * 70)
        print("Planner Raw Response")
        print("=" * 70)
        print(response)

        data = json.loads(response)

        # Normalize action names
        action = data.get("action", "").strip()
        data["action"] = ACTION_ALIASES.get(action, action)

        return ExecutionCommand(**data)