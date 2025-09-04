import argparse
from typing import List, Tuple, Optional
import boto3
from botocore.exceptions import ClientError, BotoCoreError

def make_client(region: str):
    return boto3.client("ec2", region_name=region)

def list_instances(ec2_client) -> List[dict]:
    rows = []
    try:
        paginator = ec2_client.get_paginator("describe_instances")
        for page in paginator.paginate():
            for res in page.get("Reservations", []):
                for inst in res.get("Instances", []):
                    rows.append({
                        "InstanceId": inst["InstanceId"],
                        "InstanceType": inst.get("InstanceType"),
                        "State": inst.get("State", {}).get("Name")
                    })

    except (ClientError, BotoCoreError) as e:
        print(f"Error listing instances: {e}")

    return rows


def get_latest_ami(ec2_client) -> Tuple[str, str]:
    """Prefer Amazon Linux 2023 (x86_64); fallback to Amazon Linux 2. Return Image ID and Image Name"""
    def _find(name_pattern: str) -> Tuple[Optional[str], Optional[str]]:
        resp = ec2_client.describe_images(
            Owners = ["amazon"],
            Filters = [
                {"Name" : "name", "Values" : [name_pattern]},
                {"Name" : "architecture", "Values" : ["x86_64"]},
                {"Name" : "state", "Values" : ["available"]} 
            ],
        )
        images = sorted(resp.get("Images", []), key=lambda x: x["CreationDate"], reverse = True)
        if not images:
            return None, None

        top = images[0]
        return top["ImageId"], top["Name"]

    image_id, image_name = _find("al2023-ami-*-x86_64")
    if image_id:
        return image_id, image_name

    image_id, image_name = _find("amzn2-ami-hvm-*-86_64-gp2")
    if not image_id:
        raise RuntimeError("No Suitable Amazon Linux AMI found (al2023/AL2)")

    return image_id, image_name


INSTANCE_FILE = "instance_id.txt"

def save_instance_id(instance_id: str, path: str = INSTANCE_FILE) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(instance_id.strip())

def launch_instance(ec2_client, image_id: str, instance_type: str, name_tag: str) -> str:
    resp = ec2_client.run_instances(
        ImageId=image_id,
        InstanceType=instance_type,
        MinCount=1,
        MaxCount=1,
        TagSpecifications=[{
            "ResourceType": "instance",
            "Tags": [{"Key": "Name", "Value": name_tag}],
        }],
    )
    return resp["Instances"][0]["InstanceId"]

def wait_for_state(ec2_client, instance_id: str, target: str):
    waiter_map = {
        "running": "instance_running",
        "stopped": "instance_stopped",
        "terminated": "instance_terminated",
    }
    if target not in waiter_map:
        raise ValueError(f"Unsupported target state: {target}")
    waiter = ec2_client.get_waiter(waiter_map[target])
    waiter.wait(InstanceIds=[instance_id])

def stop_instance(ec2_client, instance_id: str):
    ec2_client.stop_instances(InstanceIds=[instance_id])

def terminate_instance(ec2_client, instance_id: str):
    ec2_client.terminate_instances(InstanceIds=[instance_id])


def main():
    region="ca-central-1"
    ec2 = make_client(region)
    print(f"Region: {region}")

    print("\n Step1: List all the Instances:")
    for r in list_instances(ec2):
        print(f"- {r['InstanceId']} | {r['InstanceType']} | {r['State']}")
    
    print("\n Step2: Find Latest Amazon Linux AMI ==")
    image_id, image_name = get_latest_ami(ec2)
    print(f"Latest AMI = {image_name} ({image_id})")

    print("\n== Step 3: Launch an instance ==")
    instance_type = "t2.micro"          # change to "t3.micro" if t2 not available
    name_tag = "w3d3-ec2-demo"
    iid = launch_instance(ec2, image_id, instance_type, name_tag)
    print(f"Launched: {iid}")
    save_instance_id(iid)
    print("Saved to instance_id.txt")

    print("\n== Step 4: Wait for running ==")
    wait_for_state(ec2, iid, "running")
    print("Instance is running")

    print("\n== Step 5: Stop instance ==")
    stop_instance(ec2, iid)
    print("Stop requested; waiting for 'stopped' ...")
    wait_for_state(ec2, iid, "stopped")
    print("Instance is stopped")

    print("\n== Step 6: Terminate instance ==")
    terminate_instance(ec2, iid)
    print("Terminate requested; waiting for 'terminated' ...")
    wait_for_state(ec2, iid, "terminated")
    print("Instance is terminated")

if __name__ == "__main__":
    main()