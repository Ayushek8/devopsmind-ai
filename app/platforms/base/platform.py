from abc import ABC, abstractmethod


class Platform(ABC):

    # -------------------------------------
    # Workflows
    # -------------------------------------

    @abstractmethod
    def list_workflows(self):
        pass

    @abstractmethod
    def trigger_pipeline(
        self,
        workflow,
        branch,
        inputs=None
    ):
        pass

    # -------------------------------------
    # Runs
    # -------------------------------------

    @abstractmethod
    def latest_run(
        self,
        workflow
    ):
        pass

    @abstractmethod
    def run_history(
        self,
        workflow,
        limit=10
    ):
        pass

    # -------------------------------------
    # Jobs
    # -------------------------------------

    @abstractmethod
    def jobs(
        self,
        run_id
    ):
        pass

    @abstractmethod
    def failed_job(
        self,
        run_id
    ):
        pass

    # -------------------------------------
    # Logs
    # -------------------------------------

    @abstractmethod
    def download_logs(
        self,
        run_id
    ):
        pass

    # -------------------------------------
    # Retry
    # -------------------------------------

    @abstractmethod
    def retry(
        self,
        run_id
    ):
        pass

    # -------------------------------------
    # Cancel
    # -------------------------------------

    @abstractmethod
    def cancel(
        self,
        run_id
    ):
        pass