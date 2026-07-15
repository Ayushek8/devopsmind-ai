from app.platforms.github.github_platform import GitHubPlatform

from app.services.github.analysis.failed_step_service import FailedStepService
from app.services.github.logs.log_service import LogService

from app.services.analysis.context_extractor import ContextExtractor
from app.services.analysis.log_normalizer import LogNormalizer

from app.services.rca.rca_service import RCAService


class InvestigationService:

    def __init__(self):

        self.platform = GitHubPlatform()

        self.failed_step = FailedStepService()

        self.logs = LogService()

        self.extractor = ContextExtractor()

        self.normalizer = LogNormalizer()

        self.rca = RCAService()

    # -------------------------------------------------------

    def latest_failure(self):

        history = self.platform.run_history(

            "ci.yml",

            limit=20

        )

        failed_run = None

        for run in history:

            if run["conclusion"] == "failure":

                failed_run = run

                break

        if failed_run is None:

            return {

                "type": "incident",

                "response": {

                    "title": "No Failed Deployment",

                    "summary": "No failed workflow found.",

                    "severity": "INFO"

                }

            }

        # ------------------------------------

        job = self.platform.failed_job(

            failed_run["id"]

        )

        step = self.failed_step.detect(

            job

        )

        # ------------------------------------
        # Download Logs
        # ------------------------------------

        logs = self.logs.extract(

            failed_run["id"]

        )

        # ------------------------------------
        # Extract Context
        # ------------------------------------

        contexts = self.extractor.extract(

            logs

        )

        if not contexts:

            return {

                "type": "incident",

                "response": {

                    "title": "No Error Context",

                    "summary": "Logs downloaded but no error context found.",

                    "severity": "LOW"

                }

            }

        # ------------------------------------
        # Normalize
        # ------------------------------------

        context = self.normalizer.normalize(

            contexts[0]["context"]

        )

        # ------------------------------------
        # AI RCA
        # ------------------------------------

        incident = self.rca.analyze(

            context

        )

        # ------------------------------------

        return {

            "type": "incident",

            "response": {

                "run": failed_run,

                "job": job,

                "step": step,

                "incident": incident

            }

        }