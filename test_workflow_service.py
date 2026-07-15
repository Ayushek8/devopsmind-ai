from app.services.github.workflows.workflow_service import WorkflowService

service = WorkflowService()

print("=" * 80)

print("WORKFLOWS")

print("=" * 80)

for workflow in service.list():

    print(workflow)