from app.services.llm_service import LLMService

from app.ai.rca.log_analyzer import LogAnalyzer


class RootCauseAnalyzer:

    def __init__(self):

        self.llm = LLMService()

        self.parser = LogAnalyzer()

    def analyze(self, logs: str):

        prepared_logs = self.parser.prepare(logs)

        prompt = f"""
You are a Senior DevOps Engineer.

Analyze the deployment logs.

Return:

1. Root Cause

2. Why it happened

3. Suggested Fix

4. Commands

5. Confidence (0-100%)

Logs:

{prepared_logs}
"""

        return self.llm.ask(prompt)