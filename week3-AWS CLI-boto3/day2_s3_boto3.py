import uuid
import boto3
from  botocore.exceptions import ClientError

REGION = "us-east-1" # keep simple for free-tier demo

def make_bucket_name(prefix: str = "charles-w3d2") -> str:
    # Use a UUID to ensure the bucket name is unique
    return f"{prefix}-{uuid.uuid4().hex[:8]}"

def create_bucket(s3_client, bucket_name: str):
    """
    Creates an S3 bucket us-east-1 (no Location constraint needed here)
    """
    return s3_client.create_bucket(Bucket=bucket_name)

def upload_file(s3_client, bucket: str, local_path: str, key:str):
    """
    Uploads a local file to the specified S3 bucket under the given key.
    """
    return s3_client.upload_file(local_path, bucket, key)

def list_objects(s3_client, bucket: str):
    """
    Lists objects in the specified S3 bucket (handles empty buckets gracefully).
    """
    resp = s3_client.list_objects_v2(Bucket=bucket)
    content = resp.get("Contents", [])
    return [obj["Key"] for obj in content]

def download_file(s3_client, bucket: str, key: str, local_path: str):
    """
    Downloads a file from the specified S3 bucket to a local path.
    """
    return s3_client.download_file(bucket, key, local_path)

def cleanup_bucket(s3_client, bucket: str):
    """
    Deletes all objects in the specified S3 bucket and then deletes the bucket itself.
    """
    resp = s3_client.list_objects_v2(Bucket=bucket)
    for obj in resp.get("Contents", []):
        s3_client.delete_object(Bucket=bucket, Key=obj["Key"])
    
    # Delete the bucket
    s3_client.delete_bucket(Bucket=bucket)

def main():
    s3_client = boto3.client("s3", region_name=REGION)
    bucket = make_bucket_name()
    key1 = "sample1_s3.txt"
    key2 = "sample2_s3.txt"

    print(f"Region: {REGION}")
    print(f"Creating bucket: {bucket}")

    try:
        create_bucket(s3_client, bucket)
        print(f"Bucket {bucket} created successfully.") 

        print(f"Uploading {key1}...")
        upload_file(s3_client,bucket,"sample1.txt", key1)
        print(f"File {key1} uploaded successfully.")

        print(f"Uploading {key2}...")
        upload_file(s3_client,bucket,"sample2.txt", key2)
        print(f"File {key2} uploaded successfully.")

        print(f"Listing objects...")
        keys = list_objects(s3_client, bucket)
        print(f"Objects in bucket {bucket}: {keys}")

        print(f"Downloading {key1} to local file...")
        download_file(s3_client, bucket, key1, "downloaded_sample1.txt")
        print(f"File {key1} downloaded successfully.")

        print(f"Downloading {key2} to local file...")
        download_file(s3_client, bucket, key2, "downloaded_sample2.txt")
        print(f"File {key2} downloaded successfully.")

    except ClientError as e:
        print(f"AWS Error: {e.response.get('Error', {}).get('code')} - {e}")
        
    except Exception as e:
        print(f"Unexpected error: {e}")
        
    finally:
        print(f"Cleaning up Bucket & Object...")
        try:
            cleanup_bucket(s3_client, bucket)
        except ClientError as e:
            # If creation failed earlier, the bucket might not exist; handle gracefully
            err_code = e.response.get('Error', {}).get('Code')
            if err_code == 'NoSuchBucket':
                print("Cleanup Skipped: Bucket was never created.")
            else:
                print(f"Cleanup Error: {err_code} - {e}")

if __name__ == "__main__":
    main()