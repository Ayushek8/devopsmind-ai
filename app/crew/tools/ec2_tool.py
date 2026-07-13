from crewai.tools import BaseTool

from app.engine.talkops_engine import TalkOpsEngine


class EC2Tool(BaseTool):

    name: str = "EC2 Tool"

    description: str = (
        "Execute AWS EC2 operations."
    )

    def _run(self, command: str):

        engine = TalkOpsEngine()

        return engine.execute(command)
