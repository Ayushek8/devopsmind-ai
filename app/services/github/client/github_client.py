import os
import requests

from github import Github
from dotenv import load_dotenv

load_dotenv()


class GitHubClient:

    def __init__(self):

        self.token = os.getenv("GITHUB_TOKEN")

        self.owner = os.getenv("GITHUB_OWNER")

        self.repo = os.getenv("GITHUB_REPO")

        self.github = Github(self.token)

        self.repository = self.github.get_repo(
            f"{self.owner}/{self.repo}"
        )

        self.base_url = (
            f"https://api.github.com/repos/"
            f"{self.owner}/{self.repo}"
        )

        self.headers = {

            "Authorization": f"Bearer {self.token}",

            "Accept": "application/vnd.github+json"

        }

    # -------------------------------------------------
    # HTTP METHODS
    # -------------------------------------------------

    def get(self, endpoint):

        response = requests.get(

            self.base_url + endpoint,

            headers=self.headers

        )

        response.raise_for_status()

        return response.json()

    def post(

        self,

        endpoint,

        payload

    ):

        response = requests.post(

            self.base_url + endpoint,

            headers=self.headers,

            json=payload

        )

        response.raise_for_status()

        return response

    # -------------------------------------------------
    # Repository
    # -------------------------------------------------

    def repository_object(self):

        return self.repository