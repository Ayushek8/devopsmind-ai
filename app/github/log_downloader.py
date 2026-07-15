from app.executors.github.github_executor import GitHubExecutor


class LogDownloader:

    def __init__(self):

        self.executor = GitHubExecutor()

    # --------------------------------------------------------

    def get_run(self, run_id):

        return self.executor.get_run(run_id)

    # --------------------------------------------------------

    def get_jobs(self, run_id):

        return self.executor.get_jobs(run_id)

    # --------------------------------------------------------

    def failed_job(self, run_id):

        run = self.get_run(run_id)

        print("=" * 80)
        print("WORKFLOW RUN")
        print("=" * 80)

        print(f"Run ID     : {run['id']}")
        print(f"Status     : {run['status']}")
        print(f"Conclusion : {run['conclusion']}")

        if run["conclusion"] == "success":

            print("\nWorkflow completed successfully.")
            print("No failed jobs exist.")

            return None

        jobs = self.get_jobs(run_id)

        print("=" * 80)
        print("ALL JOBS")
        print("=" * 80)

        for job in jobs.get("jobs", []):

            print(f"Job        : {job['name']}")
            print(f"Status     : {job['status']}")
            print(f"Conclusion : {job['conclusion']}")
            print("-" * 80)

        for job in jobs.get("jobs", []):

            if job["conclusion"] == "failure":

                print("\nFailed Job Found")

                return job

        print("\nNo failed jobs found.")

        return None