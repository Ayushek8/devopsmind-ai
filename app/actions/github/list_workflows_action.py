from app.actions.github.base_action import BaseAction


class ListWorkflowsAction(BaseAction):

    def execute(

        self,

        command,

        platform

    ):

        workflows = platform.list_workflows()

        return {

            "type": "workflows",

            "response": workflows

        }