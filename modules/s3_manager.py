import boto3

s3 = boto3.client('s3')

def list_buckets():
    response = s3.list_buckets()
    if not response['Buckets']:
        print("No buckets found.")
        return
    for bucket in response['Buckets']:
        print(f"Bucket: {bucket['Name']}")

if __name__ == "__main__":
    list_buckets()
