import time

from app.executors.github.github_executor import GitHubExecutor


class GitHubMonitor:

    def __init__(self):

        self.executor = GitHubExecutor()

    def monitor(
        self,
        workflow_file
    ):

        run = self.executor.latest_run(
            workflow_file
        )

        if run is None:

            print("No workflow runs found.")
            return None

        run_id = run["id"]

        print("=" * 60)
        print(f"Monitoring Run ID : {run_id}")
        print("=" * 60)

        while True:

            current = self.executor.get_run(
                run_id
            )

            print(
                f"Status : {current['status']}"
            )

            if current["status"] == "completed":

                print(
                    f"Conclusion : {current['conclusion']}"
                )

                return current

            time.sleep(5)
