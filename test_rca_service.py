from app.services.github.history.history_service import HistoryService
from app.services.github.logs.log_service import LogService

from app.services.analysis.context_extractor import ContextExtractor
from app.services.analysis.log_normalizer import LogNormalizer

from app.services.rca.rca_service import RCAService


history = HistoryService()

failed = next(

    run

    for run in history.latest(limit=20)

    if run["conclusion"] == "failure"

)

logs = LogService().extract(

    failed["id"]

)

contexts = ContextExtractor().extract(

    logs

)

if not contexts:

    print("No context found.")

    exit()

context = contexts[0]["context"]

normalized = LogNormalizer().normalize(

    context

)

result = RCAService().analyze(

    normalized

)

print("=" * 80)

print("AI RCA")

print("=" * 80)

print()

for key, value in result.items():

    print(f"{key} : {value}")