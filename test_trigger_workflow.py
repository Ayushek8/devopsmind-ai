from app.services.github.client.github_client import GitHubClient

client = GitHubClient()

result = client.trigger_workflow(
    workflow_file="ci.yml",
    ref="feature/crewai-integration"
)

print("=" * 70)
print("Trigger Workflow")
print("=" * 70)

print(result)
