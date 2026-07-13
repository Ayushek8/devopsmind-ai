from app.services.llm_service import LLMService


class DeploymentSummary:

    def __init__(self):

        self.llm = LLMService()

    def summarize(self, run):

        prompt = f"""
You are a Principal DevOps Engineer.

Analyze the following GitHub Actions workflow execution.

Generate a professional deployment summary.

Include:

1. Workflow Name

2. Repository

3. Branch

4. Commit ID

5. Triggered By

6. Status

7. Conclusion

8. Started Time

9. Updated Time

10. Overall Assessment

11. Recommendations

Workflow JSON

{run}

Return Markdown.
"""

        return self.llm.ask(prompt)
