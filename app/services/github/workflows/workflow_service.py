from app.services.github.client.github_client import GitHubClient


class WorkflowService:

    def __init__(self):

        self.client = GitHubClient()

    # ----------------------------------------

    def list(self):

        workflows = self.client.repository_object().get_workflows()

        result = []

        for workflow in workflows:

            result.append(

                {

                    "id": workflow.id,

                    "name": workflow.name,

                    "path": workflow.path,

                    "state": workflow.state

                }

            )

        return result

    # ----------------------------------------

    def trigger(

        self,

        workflow,

        branch,

        inputs=None

    ):

        payload = {

            "ref": branch

        }

        if inputs:

            payload["inputs"] = inputs

        self.client.post(

            f"/actions/workflows/{workflow}/dispatches",

            payload

        )

        return {

            "success": True,

            "workflow": workflow,

            "branch": branch

        }