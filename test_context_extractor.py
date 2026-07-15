from app.services.github.history.history_service import HistoryService
from app.services.github.logs.log_service import LogService

from app.services.analysis.context_extractor import ContextExtractor


history = HistoryService()

runs = history.latest(limit=20)

failed = next(

    (

        run

        for run in runs

        if run["conclusion"] == "failure"

    ),

    None

)

if failed is None:

    print("No failed runs found.")

    exit()

print(f"Using Run : {failed['id']}")

logs = LogService().extract(

    failed["id"]

)

extractor = ContextExtractor()

contexts = extractor.extract(

    logs

)

print("=" * 80)

print(f"FOUND {len(contexts)} CONTEXTS")

print("=" * 80)

for item in contexts:

    print()

    print(item["file"])

    print("-" * 80)

    print(item["keyword"])

    print()

    print(item["context"][:1500])

    print()

    print("=" * 80)