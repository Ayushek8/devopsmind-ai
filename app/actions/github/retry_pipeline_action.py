from app.actions.github.base_action import BaseAction


class RetryPipelineAction(BaseAction):

    def execute(

        self,

        command,

        platform

    ):

        workflow = "ci.yml"

        latest = platform.latest_failed_run(

            workflow

        )

        if latest is None:

            return {

                "type": "text",

                "response": "No failed pipeline found."

            }

        result = platform.retry(

            latest["id"]

        )

        return {

            "type": "deployment",

            "response": {

                "message": "Pipeline retry triggered successfully.",

                "workflow": workflow,

                "run_id": latest["id"],

                "status": "queued",

                "github_response": result

            }

        }