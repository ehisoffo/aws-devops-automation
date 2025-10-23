import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

# List all running instances
def list_instances():
    response = ec2.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print(f"Instance ID: {instance['InstanceId']} | State: {instance['State']['Name']}")

# Start an EC2 instance
def start_instance(instance_id):
    ec2.start_instances(InstanceIds=[instance_id])
    print(f"Starting instance: {instance_id}")

# Stop an EC2 instance
def stop_instance(instance_id):
    ec2.stop_instances(InstanceIds=[instance_id])
    print(f"Stopping instance: {instance_id}")

# Example usage
if __name__ == "__main__":
    list_instances()
    # start_instance("i-0abcd1234efgh5678")
