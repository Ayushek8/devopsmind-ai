from app.state.session_manager import session_manager


class DeploymentContext:

    def save(

        self,

        workflow,

        run_id,

        branch,

        status,

        platform="github"

    ):

        session_manager.update(

            workflow=workflow,

            run_id=run_id,

            branch=branch,

            status=status,

            platform=platform

        )

    def current(self):

        return session_manager.get()