
import os
import boto3
from botocore.exceptions import ClientError

import settings

aws_region = os.getenv(key=settings.aws_region)
s3_client = boto3.client('s3', region_name=aws_region)
ssm_client = boto3.client('ssm', region_name=aws_region)
bucket_name = os.getenv(key=settings.bucket_name)

# Define the function to get the ssm parameters
def get_ssm_parameter(parameter_name):
    try:
        response = ssm_client.get_parameter(
            Name=parameter_name,
            WithDecryption=True
        )["Parameter"]["Value"]
        return response
    except (Exception, ClientError) as e:
        print(f'ERROR: {e}, Parameter name: {parameter_name}!')
        return None

# Function to upload file to S3 bucket
def upload_to_s3(file):
    print(f'INFO: Uploading file to s3...')
    upload_key = f'upload/{file.filename}'
    try:
        s3_client.upload_fileobj(
            Fileobj=file,
            Bucket=bucket_name,
            Key=upload_key
        )
        print(f'INFO: File successfully uploaded to s3 with the key: {upload_key}')
        return True
    except (ClientError, Exception) as e:
        print(f'ERROR: {e}!')
        return False

