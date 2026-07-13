from app.router.intent_router import IntentRouter

router = IntentRouter()

commands = [
    "Create an EC2 instance",
    "Trigger Jenkins pipeline",
    "Scale Kubernetes deployment",
    "Review Dockerfile",
    "Create Git branch",
    "Hello DevOpsMind"
]

print("=" * 50)
print("Testing Intent Router")
print("=" * 50)

for command in commands:
    print(f"\nCommand : {command}")
    print(f"Intent  : {router.detect(command).value}")
