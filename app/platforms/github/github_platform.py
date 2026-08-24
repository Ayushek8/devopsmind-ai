from app.platforms.base.platform import Platform

from app.services.github.workflows.workflow_service import WorkflowService
from app.services.github.runs.run_service import RunService
from app.services.github.jobs.job_service import JobService
from app.services.github.logs.log_service import LogService
from app.services.github.history.history_service import HistoryService


class GitHubPlatform(Platform):

    def __init__(self):

        self.workflow = WorkflowService()
        self.run = RunService()
        self.job = JobService()
        self.log = LogService()
        self.history = HistoryService()

    # ----------------------------------------------------
    # Workflows
    # ----------------------------------------------------

    def list_workflows(self):

        return self.workflow.list()

    def trigger_pipeline(

        self,

        workflow,

        branch,

        inputs=None

    ):

        return self.workflow.trigger(

            workflow,

            branch,

            inputs

        )

    # ----------------------------------------------------
    # Runs
    # ----------------------------------------------------

    def latest_run(

        self,

        workflow

    ):

        return self.run.latest(

            workflow

        )

    def run_history(

        self,

        workflow,

        limit=10

    ):

        return self.history.latest(

            workflow,

            limit

        )

    def list_runs(

        self,

        workflow=None,

        limit=20

    ):

        return self.run.list_runs(

            workflow,

            limit

        )

    def latest_failed_run(

        self,

        workflow,

        limit=20

    ):

        history = self.history.latest(

            workflow,

            limit

        )

        for run in history:

            if run["conclusion"] == "failure":

                return run

        return None

    # ----------------------------------------------------
    # Jobs
    # ----------------------------------------------------

    def jobs(

        self,

        run_id

    ):

        return self.job.list(

            run_id

        )

    def failed_job(

        self,

        run_id

    ):

        return self.job.failed(

            run_id

        )

    # ----------------------------------------------------
    # Logs
    # ----------------------------------------------------

    def download_logs(

        self,

        run_id

    ):

        return self.log.download(

            run_id

        )

    # ----------------------------------------------------
    # Retry
    # ----------------------------------------------------

    def retry(

        self,

        run_id

    ):

        return self.run.retry(

            run_id

        )

    # ----------------------------------------------------
    # Cancel
    # ----------------------------------------------------

    def cancel(

        self,

        run_id

    ):

        return self.run.cancel(

            run_id

        )