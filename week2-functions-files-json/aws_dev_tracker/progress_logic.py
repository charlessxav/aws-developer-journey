def track_services():
    return ["S3", "Lambda", "Cloudwatch", "DynamoDB"]
    
def service_summary(services_list):
    return f"Learning AWS services: \n-" + "\n-" .join(services_list)


def add_certification(current, new=1):
    return current + new    