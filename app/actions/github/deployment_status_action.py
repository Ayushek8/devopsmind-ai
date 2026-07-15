from app.actions.github.base_action import BaseAction


class DeploymentStatusAction(BaseAction):

    def execute(

        self,

        command,

        platform

    ):

        latest = platform.latest_run(

            "ci.yml"

        )

        if latest is None:

            return {

                "type": "text",

                "response": "No deployment found."

            }

        return {

            "type": "deployment_status",

            "response": {

                "workflow": latest["name"],

                "branch": latest["head_branch"],

                "status": latest["status"],

                "conclusion": latest["conclusion"],

                "event": latest["event"],

                "run_id": latest["id"],

                "url": latest["html_url"]

            }

        }