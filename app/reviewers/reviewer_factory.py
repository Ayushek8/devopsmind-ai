from app.reviewers.jenkins_reviewer import JenkinsReviewer


class ReviewerFactory:

    @staticmethod
    def get(file_type: str):

        if file_type == "jenkins":

            return JenkinsReviewer()

        raise Exception(
            "Unsupported reviewer."
        )
