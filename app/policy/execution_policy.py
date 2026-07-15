from app.policy.action_type import ActionType


class ExecutionPolicy:

    WRITE_ACTIONS = {

        "deploy",
        "trigger_pipeline",
        "rollback",
        "terminate",
        "delete",
        "destroy",
        "restart",
        "scale",
        "create",
        "update"

    }

    READ_ACTIONS = {

        "list",
        "show",
        "describe",
        "status",
        "monitor",
        "history",
        "logs",
        "review",
        "analyze"

    }

    @classmethod
    def get_action_type(cls, action: str):

        action = action.lower()

        if action in cls.WRITE_ACTIONS:

            return ActionType.WRITE

        return ActionType.READ

    @classmethod
    def requires_confirmation(cls, action: str):

        return cls.get_action_type(action) == ActionType.WRITE
