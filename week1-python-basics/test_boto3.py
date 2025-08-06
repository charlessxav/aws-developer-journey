import boto3

s3 = boto3.client('s3')
response = s3.list_buckets()

print("Buckets:")
for bucket in response['Buckets']:
    print(f"  {bucket['Name']}")
# This code lists all S3 buckets in the AWS account using Boto3.
# Ensure you have the necessary AWS credentials configured to run this code.