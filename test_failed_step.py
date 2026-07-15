from app.platforms.github.github_platform import GitHubPlatform
from app.services.github.analysis.failed_step_service import FailedStepService

platform = GitHubPlatform()

RUN_ID = 29446332397

job = platform.failed_job(RUN_ID)

step = FailedStepService().detect(job)

print("=" * 80)
print("FAILED STEP")
print("=" * 80)

print(step)