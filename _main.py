import boto3
import _aws_login

def list_instances():
    nb_ec2 = 0
    client = boto3.client('ec2')

    instances = client.describe_instances(Filters=[{
        # 'Name' :'instance-state-name', 'Values': ["running"]
        }])
    for instance in instances['Reservations']:
        nb_ec2 += 1
    print('EC2 number:', nb_ec2)

list_instances()

def list_ecs_instances_with_ec2():

    client = boto3.client('ecs')
    instances = client.list_services(launchType='EC2')
    print('ecs:', instances)

list_ecs_instances_with_ec2()