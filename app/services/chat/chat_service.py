from app.ai.planner import Planner
from app.executors.github.github_executor import GitHubExecutor
from app.monitor.github_monitor import GitHubMonitor
from app.ai.deployment_summary import DeploymentSummary


class ChatService:

    def __init__(self):

        self.planner = Planner()

        self.github = GitHubExecutor()

        self.monitor = GitHubMonitor()

        self.summary = DeploymentSummary()

    def process(
        self,
        message: str
    ):

        text = message.lower()

        # -----------------------------
        # Deploy
        # -----------------------------

        if "deploy" in text:

            self.github.trigger_pipeline(
                workflow_file="ci.yml",
                ref="feature/crewai-integration"
            )

            run = self.monitor.monitor(
                "ci.yml"
            )

            return self.summary.summarize(run)

        # -----------------------------
        # Show Workflows
        # -----------------------------

        if "workflow" in text:

            workflows = self.github.list_workflows()

            return str(workflows)

        return "Sorry, I don't understand that command yet."
