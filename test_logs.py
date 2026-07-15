from app.services.github.logs.log_service import LogService
from app.services.github.runs.run_service import RunService

run = RunService().latest("ci.yml")

service = LogService()

logs = service.download(

    run["id"]

)

print("=" * 80)

print("Downloaded")

print("=" * 80)

print(

    len(logs)

)

print()

print(

    service.url(

        run["id"]

    )

)