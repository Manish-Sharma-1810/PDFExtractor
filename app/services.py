import boto3
from botocore.exceptions import ClientError

import settings

s3_client = boto3.client('s3', region_name=settings.aws_region)

# Function to upload file to S3 bucket
def upload_to_s3(file):
    print(f'INFO: Uploading file to s3...')
    upload_key = f'upload/{file.filename}'
    try:
        s3_client.upload_fileobj(
            Fileobj=file,
            Bucket=settings.bucket_name,
            Key=upload_key
        )
        print(f'INFO: File successfully uploaded to s3 with the key: {upload_key}')
        return True
    except (ClientError, Exception) as e:
        print(f'ERROR: {e}!')
        return False
    
# Function to list all the s3 buckets
def list_buckets():
    print(f'INFO: Listing all the s3 buckets...')
    try:
        buckets = s3_client.list_buckets()
        for bucket in buckets['Buckets']:
            print(f'INFO: {bucket["Name"]}')
    except (ClientError, Exception) as e:
        print(f'ERROR: {e}!')