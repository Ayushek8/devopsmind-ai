from app.ai.rca.root_cause_analyzer import RootCauseAnalyzer

analyzer = RootCauseAnalyzer()

logs = """
Docker build failed

Error response from daemon:

toomanyrequests:
You have reached your pull rate limit.
"""

print(analyzer.analyze(logs))