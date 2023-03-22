import boto3
import _aws_login

regions = {'us-east-1'}
client_name = 'default'

def list_instance(region,client_name):
    for region in regions:
        session = _aws_login.Authenticate("ec2",region,client_name)
        # boto3.ressource('ec2',region_name=region,)
        instances = session.describe_instances(Filters=[{'Name' :'instance-state-name', 'Values': ["running"]}])
        for instance in instances:
            print(instance.id, instance.instance_type, region, instance.tags)

list_instance(regions, client_name)