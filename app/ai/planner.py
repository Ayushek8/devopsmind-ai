from app.services.llm_service import LLMService
from app.schemas.execution_command import ExecutionCommand
from app.utils.json_parser import JSONParser


class Planner:

    def __init__(self):

        self.llm = LLMService()

    # --------------------------------------------------------

    def detect_platform(self, user_request: str):

        text = user_request.lower()

        if any(word in text for word in [
            "github",
            "workflow",
            "pipeline",
            "deploy",
            "deployment",
            "pull request",
            "commit"
        ]):

            return "github"

        if any(word in text for word in [
            "jenkins",
            "job",
            "build"
        ]):

            return "jenkins"

        if any(word in text for word in [
            "aws",
            "ec2",
            "vpc",
            "iam",
            "s3"
        ]):

            return "aws"

        if any(word in text for word in [
            "kubernetes",
            "k8s",
            "pod"
        ]):

            return "kubernetes"

        return "general"

    # --------------------------------------------------------
    # FAST RULE ENGINE
    # --------------------------------------------------------

    def rule_engine(self, message):

        text = message.lower()

        investigate_keywords = [

            "why did deployment fail",

            "deployment failed",

            "investigate deployment",

            "deployment rca",

            "root cause",

            "analyze deployment",

            "analyse deployment",

            "find deployment issue",

            "why pipeline failed"

        ]

        if any(k in text for k in investigate_keywords):

            return ExecutionCommand(

                domain="github",

                service="deployment",

                action="investigate_deployment",

                parameters={}

            )

        workflow_keywords = [

            "show workflows",

            "list workflows",

            "github workflows"

        ]

        if any(k in text for k in workflow_keywords):

            return ExecutionCommand(

                domain="github",

                service="actions",

                action="list_workflows",

                parameters={}

            )

        return None

    # --------------------------------------------------------

    def plan(self, user_request):

        # ----------------------------------------
        # Try Rule Engine First
        # ----------------------------------------

        command = self.rule_engine(

            user_request

        )

        if command:

            print("=" * 70)
            print("Rule Engine Matched")
            print("=" * 70)
            print(command)

            return command

        # ----------------------------------------
        # Otherwise Use LLM
        # ----------------------------------------

        platform = self.detect_platform(

            user_request

        )

        print("=" * 70)
        print(f"Detected Platform : {platform}")
        print("=" * 70)

        if platform == "github":

            prompt = f"""
You are a GitHub planner.

Return ONLY valid JSON.

Allowed actions:

trigger_pipeline

list_workflows

deployment_status

investigate_deployment

retry_pipeline

cancel_pipeline

Return ONLY JSON.

User Request:

{user_request}
"""

        elif platform == "jenkins":

            prompt = f"""
Return ONLY JSON.

{{
    "domain":"jenkins",
    "service":"pipeline",
    "action":"trigger_pipeline",
    "parameters":{{}}
}}

User Request:

{user_request}
"""

        elif platform == "aws":

            prompt = f"""
Return ONLY JSON.

{{
    "domain":"aws",
    "service":"ec2",
    "action":"list",
    "parameters":{{}}
}}

User Request:

{user_request}
"""

        elif platform == "kubernetes":

            prompt = f"""
Return ONLY JSON.

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
Return ONLY JSON.

{{
    "domain":"general",
    "service":"chat",
    "action":"answer",
    "parameters":{{}}
}}

User Request:

{user_request}
"""

        response = self.llm.ask(

            prompt

        )

        print("=" * 70)
        print("Planner Response")
        print("=" * 70)
        print(response)

        data = JSONParser.parse(

            response

        )

        return ExecutionCommand(

            **data

        )