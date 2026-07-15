from app.ai.planner import Planner
from app.router.intent_router import IntentRouter
from app.policy.execution_policy import ExecutionPolicy


class ChatService:

    def __init__(self):

        self.planner = Planner()
        self.router = IntentRouter()

    def process(
        self,
        message: str
    ):

        # -----------------------------
        # Convert User Message
        # into Execution Command
        # -----------------------------

        command = self.planner.plan(
            message
        )

        # -----------------------------
        # Apply Execution Policy
        # -----------------------------

        command.requires_confirmation = (
            ExecutionPolicy.requires_confirmation(
                command.action
            )
        )

        # -----------------------------
        # Temporary:
        # Auto execute
        #
        # Later we'll ask for confirmation
        # in the browser.
        # -----------------------------

        return self.router.route(
            command
        )