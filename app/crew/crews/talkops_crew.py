from crewai import Crew

from app.crew.agents.aws_crew_agent import aws_crew_agent
from app.crew.tasks.aws_tasks import get_aws_task


class TalkOpsCrew:

    def run(self, command: str):

        task = get_aws_task(command)

        crew = Crew(

            agents=[
                aws_crew_agent
            ],

            tasks=[
                task
            ],

            verbose=True
        )

        return crew.kickoff()
