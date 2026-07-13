from github import Github
from dotenv import load_dotenv

import requests
import os

load_dotenv()


class GitHubClient:

    def __init__(self):

        self.token = os.getenv("GITHUB_TOKEN")
        self.owner = os.getenv("GITHUB_OWNER")
        self.repo_name = os.getenv("GITHUB_REPO")

        self.github = Github(self.token)

        self.repo = self.github.get_repo(
            f"{self.owner}/{self.repo_name}"
        )

    # ----------------------------------------
    # List Workflows
    # ----------------------------------------

    def get_workflows(self):

        return self.repo.get_workflows()

    # ----------------------------------------
    # Trigger Workflow
    # ----------------------------------------

    def trigger_workflow(
        self,
        workflow_file: str,
        ref: str = "main",
        inputs: dict | None = None
    ):

        url = (
            f"https://api.github.com/repos/"
            f"{self.owner}/{self.repo_name}"
            f"/actions/workflows/{workflow_file}/dispatches"
        )

        headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json"
        }

        payload = {
            "ref": ref
        }

        if inputs:
            payload["inputs"] = inputs

        response = requests.post(
            url,
            headers=headers,
            json=payload
        )

        return {
            "status_code": response.status_code,
            "success": response.status_code == 204,
            "response": response.text
        }

    # ----------------------------------------
    # Get Workflow Runs
    # ----------------------------------------

    def get_workflow_runs(
        self,
        workflow_file
    ):

        url = (
            f"https://api.github.com/repos/"
            f"{self.owner}/{self.repo_name}"
            f"/actions/workflows/{workflow_file}/runs"
        )

        headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json"
        }

        response = requests.get(
            url,
            headers=headers
        )

        return response.json()

    # ----------------------------------------
    # Latest Workflow Run
    # ----------------------------------------

    def get_latest_run(
        self,
        workflow_file
    ):

        runs = self.get_workflow_runs(
            workflow_file
        )

        if runs["total_count"] == 0:
            return None

        return runs["workflow_runs"][0]

    # ----------------------------------------
    # Get Run Details
    # ----------------------------------------

    def get_run(
        self,
        run_id
    ):

        url = (
            f"https://api.github.com/repos/"
            f"{self.owner}/{self.repo_name}"
            f"/actions/runs/{run_id}"
        )

        headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json"
        }

        response = requests.get(
            url,
            headers=headers
        )

        return response.json()