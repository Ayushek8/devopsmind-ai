from app.crew.tools.ec2_tool import EC2Tool

tool = EC2Tool()

result = tool.run(
    "List all EC2 instances"
)

print(result)
