from fastapi import APIRouter
from app.context.deployment_context import DeploymentContext

router = APIRouter()

context = DeploymentContext()


@router.get("/deployment/current")
def current_deployment():

    state = context.current()

    return {
        "workflow": state.workflow,
        "run_id": state.run_id,
        "branch": state.branch,
        "status": state.status,
        "platform": state.platform
    }