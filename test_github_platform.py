from app.platforms.github.github_platform import GitHubPlatform

platform = GitHubPlatform()

print("=" * 80)
print("WORKFLOWS")
print("=" * 80)

for workflow in platform.list_workflows():

    print(workflow)

print()

print("=" * 80)
print("LATEST RUN")
print("=" * 80)

latest = platform.latest_run("ci.yml")

print(latest)