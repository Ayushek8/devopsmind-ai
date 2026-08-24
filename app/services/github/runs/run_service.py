from app.services.github.client.github_client import GitHubClient


class RunService:

    def __init__(self):

        self.client = GitHubClient()

    # ----------------------------------------------------
    # Latest Run
    # ----------------------------------------------------

    def latest(

        self,

        workflow_file

    ):

        data = self.client.get(

            f"/actions/workflows/{workflow_file}/runs"

        )

        if data["total_count"] == 0:

            return None

        return data["workflow_runs"][0]

    # ----------------------------------------------------
    # Get Run
    # ----------------------------------------------------

    def get(

        self,

        run_id

    ):

        return self.client.get(

            f"/actions/runs/{run_id}"

        )

    # ----------------------------------------------------
    # History
    # ----------------------------------------------------

    def history(

        self,

        workflow_file,

        limit=10

    ):

        data = self.client.get(

            f"/actions/workflows/{workflow_file}/runs"

        )

        result = []

        for run in data["workflow_runs"][:limit]:

            result.append(

                {

                    "id": run["id"],

                    "workflow": run["name"],

                    "branch": run["head_branch"],

                    "status": run["status"],

                    "conclusion": run["conclusion"],

                    "event": run["event"],

                    "created_at": run["created_at"],

                    "updated_at": run["updated_at"]

                }

            )

        return result

    # ----------------------------------------------------
    # List Runs (Filtered or Unfiltered)
    # ----------------------------------------------------

    def list_runs(

        self,

        workflow_file=None,

        limit=20

    ):

        if workflow_file:

            endpoint = f"/actions/workflows/{workflow_file}/runs"

        else:

            endpoint = "/actions/runs"

        data = self.client.get(endpoint)

        result = []

        for run in data.get("workflow_runs", [])[:limit]:

            commit_message = "N/A"

            if run.get("head_commit"):

                commit_message = run["head_commit"].get("message", "No commit message")

            result.append(

                {

                    "id": run["id"],

                    "workflow": run["name"],

                    "branch": run["head_branch"],

                    "status": run["status"],

                    "conclusion": run["conclusion"],

                    "event": run["event"],

                    "created_at": run["created_at"],

                    "updated_at": run["updated_at"],

                    "commit_message": commit_message,

                    "url": run.get("html_url")

                }

            )

        return result

    # ----------------------------------------------------
    # Retry Run
    # ----------------------------------------------------

    def retry(

        self,

        run_id

    ):

        return self.client.post(

            f"/actions/runs/{run_id}/rerun"

        )

    # ----------------------------------------------------
    # Cancel Run
    # ----------------------------------------------------

    def cancel(

        self,

        run_id

    ):

        return self.client.post(

            f"/actions/runs/{run_id}/cancel"

        )