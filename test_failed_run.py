from app.platforms.github.github_platform import GitHubPlatform

platform = GitHubPlatform()

RUN_ID = 29446332397

print("=" * 80)
print("FAILED JOB")
print("=" * 80)

job = platform.failed_job(RUN_ID)

print(job)