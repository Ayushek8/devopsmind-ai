from app.monitor.github_monitor import GitHubMonitor

monitor = GitHubMonitor()

result = monitor.monitor(
    "ci.yml"
)

print("=" * 70)
print("Final Result")
print("=" * 70)

print(result)
