from app.executors.aws.ec2_executor import EC2Executor

executor = EC2Executor()

print("=" * 60)

print(executor.execute("list"))
