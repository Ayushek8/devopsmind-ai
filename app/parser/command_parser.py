from dataclasses import dataclass
from typing import Dict

from app.actions.aws_actions import AWS_ACTIONS


@dataclass
class Command:

    domain: str
    service: str
    action: str
    parameters: Dict


class CommandParser:

    def parse(self, text: str) -> Command:

        text = text.lower().strip()

        if text in AWS_ACTIONS:

            action = AWS_ACTIONS[text]

            return Command(
                domain="aws",
                service=action["service"],
                action=action["action"],
                parameters={}
            )

        return Command(
            domain="unknown",
            service="unknown",
            action="unknown",
            parameters={}
        )
