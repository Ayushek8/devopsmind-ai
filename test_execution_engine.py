from app.engine.execution_engine import ExecutionEngine
from app.schemas.execution_command import ExecutionCommand

engine = ExecutionEngine()

command = ExecutionCommand(
    domain="aws",
    service="ec2",
    action="list",
    parameters={}
)

print("=" * 70)
print("Execution Engine Test")
print("=" * 70)

result = engine.execute(command)

print(result)
