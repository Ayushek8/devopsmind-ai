from nonexistent_module import Planner

planner = Planner()

tests = [

    "Deploy latest code",

    "List GitHub workflows",

    "Show deployment status",

    "Show deployment logs",

    "Retry deployment",

    "Cancel deployment",

    "Show deployment history"

]

for test in tests:

    print("=" * 80)

    print("USER:", test)

    print("=" * 80)

    command = planner.plan(test)

    print(command)

    print()