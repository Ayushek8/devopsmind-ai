class FailedStepService:

    def detect(self, job):

        if job is None:

            return None

        for step in job["steps"]:

            if step["conclusion"] == "failure":

                return {

                    "name": step["name"],

                    "number": step["number"],

                    "status": step["status"],

                    "conclusion": step["conclusion"]

                }

        return None