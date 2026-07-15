from app.services.github.history.history_service import HistoryService
from app.services.github.logs.log_service import LogService
from app.services.github.parser.error_parser import ErrorParser

history = HistoryService()

runs = history.latest(limit=20)

failed_run = next(
    (run for run in runs if run["conclusion"] == "failure"),
    None
)

if failed_run is None:
    print("No failed run found.")
    exit()

run_id = failed_run["id"]

print(f"Using Failed Run: {run_id}")

logs = LogService().extract(run_id)

parser = ErrorParser()

results = parser.extract(logs)

print("=" * 80)
print("RESULT")
print("=" * 80)

for item in results:
    print(item["file"])
    print("-" * 80)
    print(item["context"])
    print()