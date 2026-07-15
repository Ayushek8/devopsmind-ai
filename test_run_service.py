from app.services.github.runs.run_service import RunService

service = RunService()

print("=" * 80)
print("LATEST RUN")
print("=" * 80)

print(

    service.latest(
        "ci.yml"
    )

)

print()

print("=" * 80)
print("HISTORY")
print("=" * 80)

for run in service.history(

    "ci.yml",

    limit=5

):

    print(run)