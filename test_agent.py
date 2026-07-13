from app.agents.aws_agent import AWSAgent

agent = AWSAgent()

result = agent.process(
    "List all EC2 instances"
)

print(result)
