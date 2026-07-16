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

        text = message.lower().strip()

    # ----------------------------------------
    # GitHub Workflows
    # ----------------------------------------

    workflow_keywords = [

        "workflow",
        "workflows",
        "github workflow",
        "github workflows",
        "list workflow",
        "show workflow",
        "show workflows",
        "available workflows"

    ]

    if any(word in text for word in workflow_keywords):

        return ExecutionCommand(

            domain="github",
            service="actions",
            action="list_workflows",
            parameters={}

        )

    # ----------------------------------------
    # Deployment History
    # ----------------------------------------

    history_keywords = [

        "history",
        "deployment history",
        "pipeline history",
        "workflow history",
        "recent deployments",
        "recent pipelines",
        "previous deployments",
        "previous pipeline",
        "last deployments",
        "last pipeline",
        "last runs",
        "recent runs",
        "show history"

    ]

    if any(word in text for word in history_keywords):

        return ExecutionCommand(

            domain="github",
            service="actions",
            action="deployment_history",
            parameters={}

        )

    # ----------------------------------------
    # Retry Pipeline
    # ----------------------------------------

    retry_keywords = [

        "retry",
        "rerun",
        "run again",
        "deploy again",
        "retry deployment",
        "retry pipeline",
        "retry workflow",
        "rerun workflow",
        "rerun pipeline",
        "rerun deployment",
        "run failed pipeline",
        "retry latest pipeline",
        "retry latest deployment"

    ]

    if any(word in text for word in retry_keywords):

        return ExecutionCommand(

            domain="github",
            service="actions",
            action="retry_pipeline",
            parameters={}

        )

    # ----------------------------------------
    # Investigate Failure
    # ----------------------------------------

    investigate_keywords = [

        "why did deployment fail",
        "deployment failed",
        "why pipeline failed",
        "pipeline failed",
        "deployment issue",
        "pipeline issue",
        "investigate deployment",
        "investigate pipeline",
        "root cause",
        "rca",
        "analyze deployment",
        "analyse deployment",
        "show latest failed deployment",
        "show failed deployment",
        "failed deployment",
        "latest failed deployment",
        "what failed",
        "what broke"

    ]

    if any(word in text for word in investigate_keywords):

        return ExecutionCommand(

            domain="github",
            service="deployment",
            action="investigate_deployment",
            parameters={}

        )

    # ----------------------------------------
    # Deployment Status
    # ----------------------------------------

    status_keywords = [

        "deployment status",
        "pipeline status",
        "workflow status",
        "current deployment",
        "latest deployment",
        "status"

    ]

    if any(word in text for word in status_keywords):

        return ExecutionCommand(

            domain="github",
            service="actions",
            action="deployment_status",
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
