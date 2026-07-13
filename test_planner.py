from app.ai.planner import Planner

planner = Planner()

command = planner.plan(
    "List all EC2 instances"
)

print("=" * 70)
print("Execution Command")
print("=" * 70)

print(command)