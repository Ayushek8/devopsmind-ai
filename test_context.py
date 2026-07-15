from app.context.deployment_context import DeploymentContext

context = DeploymentContext()

context.save(
    workflow="ci.yml",
    run_id=987654,
    branch="feature/crewai-integration",
    status="in_progress"
)

print("=" * 60)
print("Deployment Context")
print("=" * 60)

print(context.current())
