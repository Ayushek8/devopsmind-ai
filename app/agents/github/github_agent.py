from app.actions.github.action_registry import GitHubActionRegistry
from app.platforms.github.github_platform import GitHubPlatform


class GitHubAgent:

    def __init__(self):

        self.registry = GitHubActionRegistry()

        self.platform = GitHubPlatform()

    def execute(self, command):

        action = self.registry.get(

            command.action

        )

        return action.execute(

            command,

            self.platform

        )