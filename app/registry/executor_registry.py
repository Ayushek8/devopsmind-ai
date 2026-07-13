from app.executors.aws.ec2_executor import EC2Executor


EXECUTOR_REGISTRY = {

    "aws": {

        "ec2": EC2Executor()

    }

}
