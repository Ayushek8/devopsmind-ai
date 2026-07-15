from app.actions.github.base_action import BaseAction


class TriggerPipelineAction(BaseAction):

    def execute(

        self,

        command,

        platform

    ):

        workflow = "ci.yml"

        branch = "feature/crewai-integration"

        platform.trigger_pipeline(

            workflow,

            branch

        )

        latest = platform.latest_run(

            workflow

        )

        return {

            "type": "deployment",

            "response": {

                "message": "Pipeline Triggered Successfully",

                "workflow": workflow,

                "branch": branch,

                "run_id": latest["id"],

                "status": latest["status"]

            }

        }