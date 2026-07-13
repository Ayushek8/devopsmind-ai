import boto3


class EC2Executor:

    def __init__(self, region="ap-south-1"):

        self.ec2 = boto3.client(
            "ec2",
            region_name=region
        )

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
