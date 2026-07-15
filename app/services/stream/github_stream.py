import time


class GitHubStream:

    def stream(self):

        yield "Triggering Workflow..."

        time.sleep(2)

        yield "Workflow Started"

        time.sleep(2)

        yield "Checking out repository"

        time.sleep(2)

        yield "Building Docker image"

        time.sleep(2)

        yield "Running Tests"

        time.sleep(2)

        yield "Deploying"

        time.sleep(2)

        yield "Deployment Successful"