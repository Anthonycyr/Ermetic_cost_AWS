import boto3
import _aws_login

def list_instances():
    nb_ec2 = 0
    client = boto3.client('ec2')

    instances = client.describe_instances(Filters=[{
        'Name' :'instance-state-name', 'Values': ["running"]
        }])
    for instance in instances['Reservations']:
        nb_ec2 += 1
    print('EC2 instance running:', nb_ec2)

list_instances()

#ECS with Fargate
def list_ecs_instances_with_fargate():
    nb_ecs_fargate = 0
    client = boto3.client('ecs')
    tasks = client.list_task_definitions(status='ACTIVE')
    
    for task in tasks['taskDefinitionArns']:
        nb_ecs_fargate += 1
    print('ECS active task using Fargate:', nb_ecs_fargate)

list_ecs_instances_with_fargate()

# Lambda

def list_lambda():
    nb_lambda = 0
    client = boto3.client('lambda')
    functions = client.list_functions()
    for function in functions['Functions']:
        nb_lambda += 1
    print('Lambda number:',nb_lambda)

list_lambda()




# #ECS with EC2 unTested
# def list_ecs_instances_with_ec2():
#     nb_ecs_ec2 = 0
#     client = boto3.client('ecs')
#     instances = client.list_services(launchType='EC2')
    
#     for instance in instances['Reservations']:
#         nb_ecs_ec2 += 1
#     print('ECS using EC2:', nb_ecs_ec2)

# list_ecs_instances_with_ec2()



