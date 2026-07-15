from app.context.deployment_context import DeploymentContext


class DashboardService:

    def __init__(self):

        self.context = DeploymentContext()

    def get_dashboard(self):

        state = self.context.current()

        return {

            "workflow": state.workflow,

            "branch": state.branch,

            "run_id": state.run_id,

            "status": state.status,

            "platform": state.platform

        }
