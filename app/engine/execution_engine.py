from app.platforms.factory.platform_factory import PlatformFactory


class ExecutionEngine:

    def __init__(self):

        self.factory = PlatformFactory()

    # --------------------------------------------------

    def execute(

        self,

        command,

        action

    ):

        platform = self.factory.get(

            command.domain

        )

        return action.execute(

            command,

            platform

        )