from app.state.session_state import SessionState


class SessionManager:

    def __init__(self):

        self.state = SessionState()

    def update(

        self,

        workflow=None,

        run_id=None,

        branch=None,

        status=None,

        platform=None

    ):

        if workflow is not None:
            self.state.workflow = workflow

        if run_id is not None:
            self.state.run_id = run_id

        if branch is not None:
            self.state.branch = branch

        if status is not None:
            self.state.status = status

        if platform is not None:
            self.state.platform = platform

    def get(self):

        return self.state


# -------------------------------------------------
# Global Singleton
# -------------------------------------------------

session_manager = SessionManager()