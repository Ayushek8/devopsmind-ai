from app.monitor.github_monitor import GitHubMonitor
from app.ai.deployment_summary import DeploymentSummary


monitor = GitHubMonitor()

run = monitor.monitor(
    "ci.yml"
)

summary = DeploymentSummary()

result = summary.summarize(run)

print("=" * 80)
print("AI Deployment Summary")
print("=" * 80)

print(result)
