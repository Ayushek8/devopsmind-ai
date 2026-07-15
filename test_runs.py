from app.executors.github.github_executor import GitHubExecutor

executor = GitHubExecutor()

runs = executor.client.get_workflow_runs("ci.yml")

print("=" * 80)
print("LATEST WORKFLOW RUNS")
print("=" * 80)

for run in runs["workflow_runs"][:10]:

    print(f"Run ID     : {run['id']}")
    print(f"Status     : {run['status']}")
    print(f"Conclusion : {run['conclusion']}")
    print(f"Branch     : {run['head_branch']}")
    print("-" * 80)
