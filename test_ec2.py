from app.executors.aws.ec2_executor import EC2Executor

ec2 = EC2Executor()

instances = ec2.list_instances()

print("=" * 50)
print("EC2 Instances")
print("=" * 50)

for instance in instances:
    print(instance)
