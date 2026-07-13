from app.executors.github.github_executor import GitHubExecutor

executor = GitHubExecutor()

print("=" * 70)
print("Latest Workflow Run")
print("=" * 70)

run = executor.latest_run(
    "ci.yml"
)

print(run)
