from app.services.github.logs.log_service import LogService
from app.services.github.parser.error_parser import ErrorParser

RUN_ID = 29312690407

logs = LogService().extract(RUN_ID)

parser = ErrorParser()

errors = parser.extract(logs)

print("=" * 80)
print("FILES")
print("=" * 80)

for file in logs:

    print(file)

print()

print("=" * 80)
print("ERRORS")
print("=" * 80)

for error in errors:

    print()

    print(error["file"])

    print("-" * 80)

    print(error["error"])

    print()

    print(error["context"])