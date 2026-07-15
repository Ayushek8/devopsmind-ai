from app.actions.github.base_action import BaseAction

from app.services.investigation.investigation_service import InvestigationService


class InvestigateDeploymentAction(BaseAction):

    def __init__(self):

        self.service = InvestigationService()

    def execute(

        self,

        command,

        platform

    ):

        return self.service.latest_failure()