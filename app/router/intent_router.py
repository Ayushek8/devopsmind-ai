from app.agents.github.github_agent import GitHubAgent


class IntentRouter:

    def __init__(self):

        self.github = GitHubAgent()

    def route(self, command):

        try:

            if command.domain == "github":

                return self.github.execute(command)

            return {

                "type": "error",

                "response": f"Unsupported domain: {command.domain}"

            }

        except Exception as e:

            return {

                "type": "error",

                "response": str(e)

            }
