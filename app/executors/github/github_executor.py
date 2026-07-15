from app.services.github.client.github_client import GitHubClient


class GitHubExecutor:

    def __init__(self):

        self.client = GitHubClient()

    # ----------------------------------------------------

    def list_workflows(self):

        workflows = self.client.get_workflows()

        result = []

        for workflow in workflows:

            result.append(
                {
                    "name": workflow.name,
                    "state": workflow.state,
                    "path": workflow.path
                }
            )

        return result

    # ----------------------------------------------------

    def trigger_pipeline(
        self,
        workflow_file,
        ref
    ):

        return self.client.trigger_workflow(
            workflow_file,
            ref
        )

    # ----------------------------------------------------

    def latest_run(
        self,
        workflow_file
    ):

        return self.client.get_latest_run(
            workflow_file
        )

    # ----------------------------------------------------

    def get_run(
        self,
        run_id
    ):

        return self.client.get_run(
            run_id
        )

    # ----------------------------------------------------

    def get_jobs(
        self,
        run_id
    ):

        return self.client.get_jobs(
            run_id
        )