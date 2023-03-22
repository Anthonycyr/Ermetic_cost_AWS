import boto3
from botocore.exceptions import ClientError
from botocore.exceptions import InvalidConfigError
def Authenticate(service,region,profile):
    # dany = boto3.session.Session().available_profiles
    try:
        #Load config Profile from ~/.aws/config
        session = boto3.Session(profile_name=profile) 
        #Get credentials from ~/.aws/credentials file (maintained by Leapp)
        try:
            credentials = session.get_credentials()
        except InvalidConfigError as e:
            print("Credentials File is empty: Verify the Leapp session and retry...")
            exit()
        if  credentials:
            Access_key = credentials.access_key
            Secret_key = credentials.secret_key
            Token = credentials.token

            # Create a AWS Session with the above credentials
            session = boto3.client(
                service,
                region_name = region,
                aws_access_key_id= Access_key,
                aws_secret_access_key= Secret_key,
                aws_session_token= Token,
            )
            return session
        else:
            print("Credentials File is empty: Verify the Leapp session and retry...")
            exit()
    except ClientError as e:
        if e.response['Error']['Code'] == 'AccessDenied':
            print (e.response['Error']['Code'] + ": " + str(e.operation_name)  + "\n" + e.response['Error']['Message'])
        if "The source profile \"default\" must have credentials." in str(e):
            print("Credentials File is empty: Verify the Leapp session and retry...")
        exit()

    # listusers = session.list_users()
    # print (listusers)
    # return session
 
def check_aws_profile(client_name):
    try:
        boto3.Session(profile_name=client_name)
        return True
    except:
        return False

def get_account_id(profile):
    # dany = boto3.session.Session().available_profiles
    try:
        #Load config Profile from ~/.aws/config
        session = boto3.Session(profile_name=profile) 
        #Get credentials from ~/.aws/credentials file (maintained by Leapp)
        try:
            credentials = session.get_credentials()
        except InvalidConfigError as e:
            print("Credentials File is empty: Verify the Leapp session and retry...")
            exit()
        if  credentials:
            Access_key = credentials.access_key
            Secret_key = credentials.secret_key
            Token = credentials.token

            # Create a AWS Session with the above credentials
            account_id = boto3.client(
                "sts",
                aws_access_key_id=Access_key,
                aws_secret_access_key=Secret_key,
                aws_session_token=Token            
                ).get_caller_identity().get('Account')
            return account_id
        else:
            print("Credentials File is empty: Verify the Leapp session and retry...")
            exit()
    except ClientError as e:
        if e.response['Error']['Code'] == 'AccessDenied':
            print (e.response['Error']['Code'] + ": " + str(e.operation_name)  + "\n" + e.response['Error']['Message'])
        if "The source profile \"default\" must have credentials." in str(e):
            print("Credentials File is empty: Verify the Leapp session and retry...")
        exit()

#The source profile "default" must have credentials.