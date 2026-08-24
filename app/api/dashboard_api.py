from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import Optional, Dict, Any

from app.services.dashboard.dashboard_service import DashboardService
from app.platforms.github.github_platform import GitHubPlatform
from app.services.investigation.investigation_service import InvestigationService

router = APIRouter()
dashboard = DashboardService()
platform = GitHubPlatform()
investigation_service = InvestigationService()


class TriggerRequest(BaseModel):
    ref: str
    inputs: Optional[Dict[str, Any]] = None


@router.get("/dashboard")
def get_dashboard():
    return dashboard.get_dashboard()


@router.get("/github/workflows")
def get_workflows():
    try:
        workflows = platform.list_workflows()
        return {"success": True, "workflows": workflows}
    except Exception as e:
        return {"success": False, "error": str(e)}


@router.get("/github/runs")
def get_runs(workflow_file: Optional[str] = Query(None)):
    try:
        runs = platform.list_runs(workflow_file)
        return {"success": True, "runs": runs}
    except Exception as e:
        return {"success": False, "error": str(e)}


@router.get("/github/runs/{run_id}")
def get_run(run_id: int):
    try:
        run = platform.run.get(run_id)
        return {"success": True, "run": run}
    except Exception as e:
        return {"success": False, "error": str(e)}


@router.get("/github/runs/{run_id}/jobs")
def get_run_jobs(run_id: int):
    try:
        jobs = platform.jobs(run_id)
        return {"success": True, "jobs": jobs}
    except Exception as e:
        return {"success": False, "error": str(e)}


@router.get("/github/runs/{run_id}/jobs/{job_id}/logs")
def get_job_logs(run_id: int, job_id: int):
    try:
        from app.services.github.client.github_client import GitHubClient
        import requests
        client = GitHubClient()
        response = requests.get(
            f"{client.base_url}/actions/jobs/{job_id}/logs",
            headers=client.headers,
            allow_redirects=True
        )
        response.raise_for_status()
        return {"success": True, "logs": response.text}
    except Exception as e:
        return {"success": False, "error": str(e)}


@router.post("/github/workflows/{workflow_file}/trigger")
def trigger_workflow(workflow_file: str, request: TriggerRequest):
    try:
        result = platform.trigger_pipeline(
            workflow=workflow_file,
            branch=request.ref,
            inputs=request.inputs
        )
        return {"success": True, "data": result}
    except Exception as e:
        return {"success": False, "error": str(e)}


@router.post("/github/runs/{run_id}/retry")
def retry_run(run_id: int):
    try:
        result = platform.retry(run_id)
        return {"success": True, "data": result}
    except Exception as e:
        return {"success": False, "error": str(e)}


@router.post("/github/runs/{run_id}/cancel")
def cancel_run(run_id: int):
    try:
        result = platform.cancel(run_id)
        return {"success": True, "data": result}
    except Exception as e:
        return {"success": False, "error": str(e)}


@router.post("/github/runs/{run_id}/investigate")
def investigate_run(run_id: int):
    try:
        result = investigation_service.investigate_run(run_id)
        return {"success": True, "data": result.get("response")}
    except Exception as e:
        return {"success": False, "error": str(e)}
