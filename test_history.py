from app.services.github.history.history_service import HistoryService

history = HistoryService()

for run in history.latest():

    print(run)