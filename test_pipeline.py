from app.router.intent_router import IntentRouter
from app.parser.command_parser import CommandParser
from app.agents.aws_agent import AWSAgent

router = IntentRouter()
parser = CommandParser()
aws = AWSAgent()

query = "List all EC2 instances"

print("=" * 60)
print("USER INPUT")
print(query)

intent = router.detect(query)

print("\nIntent Detected:")
print(intent.value)

command = parser.parse(query)

print("\nParsed Command:")
print(command)

print("\nExecuting...")

if intent.value == "aws":

    result = aws.process(command)

    print(result)

else:

    print("No Agent Found")
