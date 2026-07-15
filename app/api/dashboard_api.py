from fastapi import APIRouter

from app.services.dashboard.dashboard_service import DashboardService

router = APIRouter()

dashboard = DashboardService()


@router.get("/dashboard")
def get_dashboard():

    return dashboard.get_dashboard()
