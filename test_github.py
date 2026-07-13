from app.executors.github.github_executor import GitHubExecutor

executor = GitHubExecutor()

print("=" * 70)
print("GitHub Workflows")
print("=" * 70)

result = executor.list_workflows()

for workflow in result:
    print(workflow)
