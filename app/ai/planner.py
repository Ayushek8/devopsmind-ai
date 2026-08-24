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

        if text == "why did deployment fail?":
            return ExecutionCommand(
                domain="github",
                service="deployment",
                action="investigate_deployment",
                parameters={}
            )

        if text in ["show workflows", "list workflows"]:
            return ExecutionCommand(
                domain="github",
                service="actions",
                action="list_workflows",
                parameters={}
            )

        if text in ["show latest failed deployment", "show latest failed run"]:
            return ExecutionCommand(
                domain="github",
                service="deployment",
                action="investigate_deployment",
                parameters={}
            )

        if text in ["show deployment history", "show run history", "show history"]:
            return ExecutionCommand(
                domain="github",
                service="actions",
                action="deployment_history",
                parameters={}
            )

        if text == "retry latest pipeline":
            return ExecutionCommand(
                domain="github",
                service="actions",
                action="retry_pipeline",
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

        prompt = f"""
You are the DevOpsMind Planner AI. Analyze the user's request (which can be in any language) and map it to the correct execution command.

Allowed domains, services and actions:

1. GitHub Actions / Deployments:
   - domain: "github"
     service: "actions"
     action: "list_workflows" (For showing/listing available workflows or pipelines)
   - domain: "github"
     service: "actions"
     action: "deployment_history" (For showing workflow runs, run history, pipeline history)
   - domain: "github"
     service: "actions"
     action: "deployment_status" (For checking the status of the latest run or pipeline)
   - domain: "github"
     service: "actions"
     action: "retry_pipeline" (For retrying, rerunning, or starting again the latest failed pipeline or workflow)
   - domain: "github"
     service: "actions"
     action: "cancel_pipeline" (For cancelling the currently running workflow or pipeline)
   - domain: "github"
     service: "actions"
     action: "trigger_pipeline" (For triggering, dispatching, or starting a new workflow run)
     parameters: {{ "workflow_file": "<filename.yml if mentioned>", "ref": "<branch name if mentioned>" }}
   - domain: "github"
     service: "deployment"
     action: "investigate_deployment" (For investigating why the latest deployment or pipeline failed, root cause analysis, or rca of build failure)

2. General Chat / SRE Q&A / Other Platforms (AWS, Jenkins, Kubernetes, Docker, generic questions, greetings, explanations):
   - domain: "general"
     service: "chat"
     action: "answer"
     parameters: {{ "question": "<the user request preserved in the user's original language>" }}

You must return ONLY a valid JSON object matching this schema:
{{
    "domain": "github" | "general",
    "service": "actions" | "deployment" | "chat",
    "action": "list_workflows" | "deployment_history" | "deployment_status" | "retry_pipeline" | "cancel_pipeline" | "trigger_pipeline" | "investigate_deployment" | "answer",
    "parameters": {{ ... }}
}}

Do not include any explanation or markdown formatting in your response. Return raw JSON only.

User Request: {user_request}
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

        print("=" * 70)
        print("Planner Parsed JSON")
        print("=" * 70)
        print(data)

        command = {
            "domain": data.get("domain", "general"),
            "service": data.get("service", "chat"),
            "action": data.get("action", "answer"),
            "parameters": data.get("parameters", {"question": user_request})
        }

        if command["action"] == "answer" and "question" not in command["parameters"]:
            command["parameters"]["question"] = user_request

        print("=" * 70)
        print("Execution Command")
        print("=" * 70)
        print(command)

        return ExecutionCommand(
            **command
        )
