import boto3
# import _aws_login

def list_instances():
    client = boto3.client('ec2')

    response = client.describe_instances()
    return response