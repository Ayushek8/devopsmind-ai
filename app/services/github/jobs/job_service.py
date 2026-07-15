from app.services.github.client.github_client import GitHubClient


class JobService:

    def __init__(self):

        self.client = GitHubClient()

    # ----------------------------------------------------

    def list(

        self,

        run_id

    ):

        jobs = self.client.get(

            f"/actions/runs/{run_id}/jobs"

        )

        return jobs["jobs"]

    # ----------------------------------------------------

    def failed(

        self,

        run_id

    ):

        jobs = self.list(run_id)

        for job in jobs:

            if job["conclusion"] == "failure":

                return job

        return None