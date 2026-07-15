from app.services.github.logs.log_service import LogService
from app.services.github.runs.run_service import RunService

run = RunService().latest("ci.yml")

service = LogService()

logs = service.extract(

    run["id"]

)

print("=" * 80)

print("FILES")

print("=" * 80)

for file in logs:

    print(file)

print()

print("=" * 80)

print("FIRST FILE")

print("=" * 80)

first = list(logs.keys())[0]

print(logs[first][:1000])