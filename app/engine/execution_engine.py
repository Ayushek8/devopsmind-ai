from app.registry.executor_registry import EXECUTOR_REGISTRY
from app.schemas.execution_command import ExecutionCommand


class ExecutionEngine:

    def execute(self, command: ExecutionCommand):

        # Get the correct executor
        executor = EXECUTOR_REGISTRY[
            command.domain
        ][
            command.service
        ]

        # Delegate execution to the executor
        return executor.execute(
            command.action,
            **command.parameters
        )
