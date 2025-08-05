my_services = ["S3", "EC2", "Lambda", "Cloudwatch", "DynamoDB"]
my_services.append("CloudFormation")
my_services.remove(my_services[1])
print(my_services)

print(f"Learning AWS services:")
for service in my_services:
    print(f"- {service}")