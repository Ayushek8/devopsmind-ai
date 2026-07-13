from crewai import Task

from app.crew.agents.aws_crew_agent import aws_crew_agent


def get_aws_task(command: str):

    return Task(

        description=f"""
Execute the following AWS request:

{command}
""",

        expected_output="""
A professional response after executing the AWS command.
""",

        agent=aws_crew_agent
    )
