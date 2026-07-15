from app.platforms.github.github_platform import GitHubPlatform
from app.services.github.analysis.failed_step_service import FailedStepService


class InvestigationService:

    def __init__(self):

        self.platform = GitHubPlatform()

        self.failed_step = FailedStepService()

    def latest_failure(self):

        history = self.platform.run_history(

            "ci.yml",

            limit=20

        )

        failed_run = None

        for run in history:

            if run["conclusion"] == "failure":

                failed_run = run

                break

        if failed_run is None:

            return None

        job = self.platform.failed_job(

            failed_run["id"]

        )

        step = self.failed_step.detect(job)

        return {

            "run": failed_run,

            "job": job,

            "step": step

        }