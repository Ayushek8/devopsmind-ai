import json

from app.services.llm_service import LLMService
from app.schemas.execution_command import ExecutionCommand
from app.utils.json_parser import JSONParser


class Planner:

    def __init__(self):

        self.llm = LLMService()

    def detect_platform(self, user_request: str):

        text = user_request.lower()

        if any(word in text for word in [
            "github",
            "workflow",
            "pipeline",
            "pull request",
            "commit",
            "deploy"
        ]):
            return "github"

        if any(word in text for word in [
            "jenkins",
            "job",
            "build"
        ]):
            return "jenkins"

        if any(word in text for word in [
            "ec2",
            "vpc",
            "s3",
            "iam",
            "aws"
        ]):
            return "aws"

        if any(word in text for word in [
            "kubernetes",
            "k8s",
            "pod",
            "deployment",
            "namespace"
        ]):
            return "kubernetes"

        return "general"

    def plan(self, user_request: str):

        platform = self.detect_platform(user_request)

        print("=" * 70)
        print(f"Detected Platform : {platform}")
        print("=" * 70)

        if platform == "github":

            prompt = f"""
You are a GitHub Actions planner.

Return ONLY valid JSON.

Never use markdown.

Never explain.

Use ONLY these actions:

trigger_pipeline
list_workflows
deployment_status
deployment_logs
deployment_history
retry_pipeline
cancel_pipeline
deployment_summary

Return exactly like this:

{{
    "domain":"github",
    "service":"actions",
    "action":"trigger_pipeline",
    "parameters":{{}}
}}

User Request:

{user_request}
"""

        elif platform == "aws":

            prompt = f"""
You are an AWS planner.

Return ONLY valid JSON.

Return exactly:

{{
    "domain":"aws",
    "service":"ec2",
    "action":"list",
    "parameters":{{}}
}}

User Request:

{user_request}
"""

        elif platform == "jenkins":

            prompt = f"""
You are a Jenkins planner.

Return ONLY valid JSON.

Return exactly:

{{
    "domain":"jenkins",
    "service":"pipeline",
    "action":"trigger_pipeline",
    "parameters":{{}}
}}

User Request:

{user_request}
"""

        elif platform == "kubernetes":

            prompt = f"""
You are a Kubernetes planner.

Return ONLY valid JSON.

Return exactly:

{{
    "domain":"kubernetes",
    "service":"deployment",
    "action":"scale",
    "parameters":{{}}
}}

User Request:

{user_request}
"""

        else:

            prompt = f"""
Return ONLY valid JSON.

{{
    "domain":"general",
    "service":"chat",
    "action":"answer",
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