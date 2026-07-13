import boto3


class EC2Executor:

    def __init__(self, region="ap-south-1"):

        self.ec2 = boto3.client(
            "ec2",
            region_name=region
        )

        self.actions = {
            "list": self.list_instances,
            "create": self.create_instance,
            "start": self.start_instance,
            "stop": self.stop_instance,
            "terminate": self.terminate_instance,
        }

    def execute(self, action, **kwargs):

        if action not in self.actions:
            raise Exception(
                f"Unsupported EC2 action: {action}"
            )

        return self.actions[action](**kwargs)

    # ---------------------------------
    # LIST
    # ---------------------------------

    def list_instances(self):

        response = self.ec2.describe_instances()

        instances = []

        for reservation in response["Reservations"]:

            for instance in reservation["Instances"]:

                instances.append(
                    {
                        "InstanceId": instance["InstanceId"],
                        "State": instance["State"]["Name"],
                        "Type": instance["InstanceType"]
                    }
                )

        return instances

    # ---------------------------------
    # CREATE
    # ---------------------------------

    def create_instance(self, **kwargs):

        return {
            "message": "Create EC2 not implemented yet."
        }

    # ---------------------------------
    # START
    # ---------------------------------

    def start_instance(self, **kwargs):

        return {
            "message": "Start EC2 not implemented yet."
        }

    # ---------------------------------
    # STOP
    # ---------------------------------

    def stop_instance(self, **kwargs):

        return {
            "message": "Stop EC2 not implemented yet."
        }

    # ---------------------------------
    # TERMINATE
    # ---------------------------------

    def terminate_instance(self, **kwargs):

        return {
            "message": "Terminate EC2 not implemented yet."
        }
