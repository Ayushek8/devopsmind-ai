from app.router.intent_router import IntentRouter
from app.parser.command_parser import CommandParser
from app.agents.aws_agent import AWSAgent
from app.formatter.response_formatter import ResponseFormatter


class TalkOpsEngine:

    def __init__(self):

        self.router = IntentRouter()
        self.parser = CommandParser()

        self.aws = AWSAgent()

        self.formatter = ResponseFormatter()

    def execute(self, user_input: str):

        intent = self.router.detect(user_input)

        command = self.parser.parse(user_input)

        if intent.value == "aws":

            result = self.aws.process(command)

            return self.formatter.format(
                user_input,
                result
            )

        return "Intent not supported yet."
