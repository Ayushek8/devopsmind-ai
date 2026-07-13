from app.executors.aws.ec2_executor import EC2Executor
from app.parser.command_parser import Command


class AWSAgent:

    def __init__(self):
        self.ec2 = EC2Executor()

    def process(self, command: Command):

        if (
            command.service == "ec2"
            and command.action == "list"
        ):
            return self.ec2.list_instances()

        return {
            "message": "AWS command not implemented yet."
        }
