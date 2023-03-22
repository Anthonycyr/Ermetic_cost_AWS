import boto3
# import _aws_login

region = 'us-east-1'

def list_instance(client_name):
    # session = _aws_login.Authenticate("cloudtrail",region,client_name)
    conn = boto3.ressource('ec2',region_name=region,)
    instances = conn.instances.filter()
    for instance in instances:
        if instance.state["Name"] == "running":
            print(instance.id, instance.instance_type, region, instance.tags)