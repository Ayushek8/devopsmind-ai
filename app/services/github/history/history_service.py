from app.services.github.runs.run_service import RunService


class HistoryService:

    def __init__(self):

        self.run = RunService()

    def latest(

        self,

        workflow="ci.yml",

        limit=10

    ):

        return self.run.history(

            workflow,

            limit

        )