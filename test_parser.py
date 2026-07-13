from app.parser.command_parser import CommandParser

parser = CommandParser()

tests = [

    "list ec2",

    "list ec2 instances",

    "describe-instances",

    "create ec2"

]

for command in tests:

    result = parser.parse(command)

    print("=" * 50)

    print(command)

    print(result)
