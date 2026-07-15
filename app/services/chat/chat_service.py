from app.ai.planner import Planner

from app.router.intent_router import IntentRouter

from app.policy.execution_policy import ExecutionPolicy

from app.core.response_builder import ResponseBuilder


class ChatService:

    def __init__(self):

        self.planner = Planner()

        self.router = IntentRouter()

    def process(

        self,

        message

    ):

        command = self.planner.plan(

            message

        )

        command.requires_confirmation = (

            ExecutionPolicy.requires_confirmation(

                command.action

            )

        )

        result = self.router.route(

            command

        )

        # Already Standard Response

        if (

            isinstance(result, dict)

            and

            "success" in result

        ):

            return result

        # Legacy Response

        if (

            isinstance(result, dict)

            and

            "type" in result

            and

            "response" in result

        ):

            return ResponseBuilder.success(

                result["type"],

                result["response"]

            )

        # String

        return ResponseBuilder.success(

            "text",

            result

        )