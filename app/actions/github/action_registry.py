from app.actions.github.list_workflows_action import ListWorkflowsAction
from app.actions.github.trigger_pipeline_action import TriggerPipelineAction
from app.actions.github.deployment_status_action import DeploymentStatusAction


class GitHubActionRegistry:

    def __init__(self):

        self.actions = {

            "list_workflows": ListWorkflowsAction(),

            "trigger_pipeline": TriggerPipelineAction(),

            "deployment_status": DeploymentStatusAction(),

        }

    def get(self, action):

        obj = self.actions.get(action)

        if obj is None:

            raise Exception(

                f"Unsupported GitHub action : {action}"

            )

        return obj