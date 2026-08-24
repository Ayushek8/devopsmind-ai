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

    # -------------------------------------------------------

    def investigate_run(self, run_id: int):

        run = self.platform.run.get(run_id)

        job = self.platform.failed_job(run_id)

        if not job:

            return {

                "type": "incident",

                "response": {

                    "run": {

                        "id": run_id,

                        "workflow": run.get("name", "Unknown"),

                        "branch": run.get("head_branch", "Unknown"),

                        "status": run.get("status"),

                        "conclusion": run.get("conclusion"),

                        "event": run.get("event"),

                        "created_at": run.get("created_at"),

                        "updated_at": run.get("updated_at")

                    },

                    "job": None,

                    "step": {

                        "name": "N/A"

                    },

                    "incident": {

                        "title": "No Failed Jobs Found",

                        "severity": "Info",

                        "root_cause": "The build does not contain any failed jobs.",

                        "summary": "This workflow run did not fail or the failed job is not accessible.",

                        "fix": "No action required.",

                        "commands": [],

                        "confidence": 100

                    }

                }

            }

        step = self.failed_step.detect(job)

        if not step:

            step = {

                "name": "Unknown Step"

            }

        # Download Logs

        try:

            logs = self.logs.extract(run_id)

        except Exception as e:

            return {

                "type": "incident",

                "response": {

                    "run": {

                        "id": run_id,

                        "workflow": run.get("name", "Unknown"),

                        "branch": run.get("head_branch", "Unknown"),

                        "status": run.get("status"),

                        "conclusion": run.get("conclusion"),

                        "event": run.get("event"),

                        "created_at": run.get("created_at"),

                        "updated_at": run.get("updated_at")

                    },

                    "job": job,

                    "step": step,

                    "incident": {

                        "title": "Logs Download Failed",

                        "severity": "Warning",

                        "root_cause": "GitHub Actions logs could not be retrieved.",

                        "summary": f"Failed to retrieve log archive: {str(e)}",

                        "fix": "Please check if the log retention period has expired or if credentials are valid.",

                        "commands": [],

                        "confidence": 50

                    }

                }

            }

        # Extract Context

        contexts = self.extractor.extract(logs)

        if not contexts:

            return {

                "type": "incident",

                "response": {

                    "run": {

                        "id": run_id,

                        "workflow": run.get("name", "Unknown"),

                        "branch": run.get("head_branch", "Unknown"),

                        "status": run.get("status"),

                        "conclusion": run.get("conclusion"),

                        "event": run.get("event"),

                        "created_at": run.get("created_at"),

                        "updated_at": run.get("updated_at")

                    },

                    "job": job,

                    "step": step,

                    "incident": {

                        "title": "No Error Context Detected",

                        "severity": "Low",

                        "root_cause": "The log files do not contain obvious error keywords.",

                        "summary": "Downloaded logs did not yield any specific error match context.",

                        "fix": "Review the full build logs manually.",

                        "commands": [],

                        "confidence": 30

                    }

                }

            }

        # Normalize

        context = self.normalizer.normalize(contexts[0]["context"])

        # AI RCA

        incident = self.rca.analyze(context)

        # Build Response

        run_data = {

            "id": run["id"],

            "workflow": run.get("name"),

            "branch": run.get("head_branch"),

            "status": run.get("status"),

            "conclusion": run.get("conclusion"),

            "event": run.get("event"),

            "created_at": run.get("created_at"),

            "updated_at": run.get("updated_at")

        }

        return {

            "type": "incident",

            "response": {

                "run": run_data,

                "job": job,

                "step": step,

                "incident": incident

            }

        }