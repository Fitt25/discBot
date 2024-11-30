from ec2_metadata import ec2_metadata

print(f"Public IP: {ec2_metadata.public_ipv4}")
print(f"Private IP: {ec2_metadata.private_ipv4}")
print(f"Availability Zone: {ec2_metadata.availability_zone}")
print(f"Region: {ec2_metadata.region}")
