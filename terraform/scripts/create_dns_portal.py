#!/usr/bin/env python3
"""
Upserts (creates or updates) a DNS A record in Route53 for a student's portal.
Example: studentmetwvraehumk.highvelocitynetworking.com → <Linux_IP>
"""

import os
import boto3
import sys
from datetime import datetime

# ---------------------------
# Setup logging
# ---------------------------
log_file = "dns_log_portal.txt"
timestamp = datetime.utcnow().isoformat()
log_lines = [f"\n--- Portal DNS Record Log [{timestamp}] ---\n"]

def log(message):
    print(message)
    log_lines.append(message + "\n")

# ---------------------------
# AWS credentials and config
# ---------------------------
aws_access_key_id = os.getenv("DEMO_AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("DEMO_AWS_SECRET_ACCESS_KEY")
region = os.getenv("AWS_REGION", "eu-central-1")
hosted_zone_id = os.getenv("PORTAL_HOSTED_ZONE_ID")
linux_ip = os.getenv("LINUX_IP")
participant_id = os.getenv("INSTRUQT_PARTICIPANT_ID", "").strip()

# ---------------------------
# Validation
# ---------------------------
if not aws_access_key_id or not aws_secret_access_key or not hosted_zone_id:
    log("❌ ERROR: Missing AWS credentials or Hosted Zone ID in environment.")
    sys.exit(1)

if not linux_ip:
    log("❌ ERROR: Linux_IP is not set in the environment.")
    sys.exit(1)

if not participant_id:
    log("⚠️  No participant ID found; using fallback record name 'portal.highvelocitynetworking.com'")
    fqdn = "portal.highvelocitynetworking.com"
else:
    fqdn = f"student{participant_id}.highvelocitynetworking.com"

# ---------------------------
# Create or update A record
# ---------------------------
log(f"➡️  Creating/Updating A record: {fqdn} → {linux_ip}")

try:
    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region
    )
    route53 = session.client("route53")

    response = route53.change_resource_record_sets(
        HostedZoneId=hosted_zone_id,
        ChangeBatch={
            "Comment": f"Upsert A record for {fqdn}",
            "Changes": [
                {
                    "Action": "UPSERT",
                    "ResourceRecordSet": {
                        "Name": fqdn,
                        "Type": "A",
                        "TTL": 300,
                        "ResourceRecords": [{"Value": linux_ip}]
                    }
                }
            ]
        }
    )

    status = response["ChangeInfo"]["Status"]
    log(f"✅  A record created/updated successfully: {fqdn} → {linux_ip}")
    log(f"📡  Change status: {status}")

except Exception as e:
    log(f"❌ Failed to create or update A record for {fqdn}: {e}")
    sys.exit(1)

# ---------------------------
# Write log to file
# ---------------------------
with open(log_file, "a") as f:
    f.writelines(log_lines)

log(f"📄 Log written to {log_file}")
