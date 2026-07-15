from app.router.intent_router import IntentRouter
from app.schemas.execution_command import ExecutionCommand

router = IntentRouter()

command = ExecutionCommand(
    domain="github",
    service="actions",
    action="list_workflows",
    parameters={}
)

print("=" * 70)
print("Router Test")
print("=" * 70)

print(router.route(command))
