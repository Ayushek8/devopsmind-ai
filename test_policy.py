from app.policy.execution_policy import ExecutionPolicy

actions = [

    "list",

    "deploy",

    "delete",

    "show",

    "restart",

    "review"

]

for action in actions:

    print("=" * 50)

    print(action)

    print(

        ExecutionPolicy.requires_confirmation(

            action

        )

    )
