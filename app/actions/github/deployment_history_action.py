from app.actions.github.base_action import BaseAction


class DeploymentHistoryAction(BaseAction):

    def execute(

        self,

        command,

        platform

    ):

        workflow = "ci.yml"

        history = platform.run_history(

            workflow,

            limit=10

        )

        return {

            "type": "history",

            "response": history

        }