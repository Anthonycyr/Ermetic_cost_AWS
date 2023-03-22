import boto3
# import _aws_login

def list_instances():
    nb_ec2 = 0
    client = boto3.client('ec2')

    instances = client.describe_instances(Filters=[{
        # 'Name' :'instance-state-name', 'Values': ["running"]
        }])
    for instance in instances:
        nb_ec2 += 1
    print(instance)

list_instances()