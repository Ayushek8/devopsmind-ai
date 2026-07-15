from app.services.github.history.history_service import HistoryService
from app.services.github.logs.log_service import LogService

from app.services.analysis.context_extractor import ContextExtractor
from app.services.analysis.log_normalizer import LogNormalizer


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

logs = LogService().extract(
    failed["id"]
)

contexts = ContextExtractor().extract(logs)

normalizer = LogNormalizer()

print("=" * 80)
print("NORMALIZED LOGS")
print("=" * 80)

for item in contexts:

    print()

    print(item["file"])

    print("-" * 80)

    print(
        normalizer.normalize(
            item["context"]
        )
    )

    print()

    print("=" * 80)