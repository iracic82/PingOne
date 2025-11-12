#!/usr/bin/env python3
"""
Adds or updates an inbound rule in a specific Security Group.
Example: allows TCP/636 from LINUX_IP (taken from env vars).

Environment variables required:
  PORTAL_AWS_ACCESS_KEY_ID
  PORTAL_AWS_ACCESS_SECRET_KEY
  AWS_REGION
  SECURITY_GROUP_ID
  LINUX_IP
"""

import os
import sys
import boto3
from datetime import datetime

# ---------------------------
# Logging setup
# ---------------------------
log_file = "sg_update_log.txt"
timestamp = datetime.utcnow().isoformat()
log_lines = [f"\n--- Security Group Update [{timestamp}] ---\n"]

def log(msg):
    print(msg)
    log_lines.append(msg + "\n")

# ---------------------------
# Env vars
# ---------------------------
aws_access_key_id     = os.getenv("PORTAL_AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("PORTAL_AWS_SECRET_ACCESS_KEY")
region                = os.getenv("AWS_REGION", "eu-central-1")
sg_id                 = os.getenv("SECURITY_GROUP_ID", "sg-09829deacde96c801")
linux_ip              = os.getenv("LINUX_IP")

if not all([aws_access_key_id, aws_secret_access_key, sg_id, linux_ip]):
    log("❌ Missing required environment variables.")
    sys.exit(1)

# ---------------------------
# Initialize boto3 EC2 client
# ---------------------------
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region
)
ec2 = session.client("ec2")

# ---------------------------
# Add inbound rule (TCP 636)
# ---------------------------
try:
    log(f"➡️  Authorizing ingress for SG {sg_id}: TCP/636 from {linux_ip}/32")
    ec2.authorize_security_group_ingress(
        GroupId=sg_id,
        IpPermissions=[
            {
                "IpProtocol": "tcp",
                "FromPort": 636,
                "ToPort": 636,
                "IpRanges": [
                    {"CidrIp": f"{linux_ip}/32", "Description": "Allow TCP 636 from LINUX_IP"}
                ],
            }
        ]
    )
    log("✅ Successfully added inbound rule.")
except ec2.exceptions.ClientError as e:
    if "InvalidPermission.Duplicate" in str(e):
        log("ℹ️  Rule already exists, skipping.")
    else:
        log(f"❌ AWS error: {e}")
        sys.exit(1)

# ---------------------------
# Write log
# ---------------------------
with open(log_file, "a") as f:
    f.writelines(log_lines)
log(f"📄 Log written to {log_file}")
