from aws_dev_tracker.user_profile import get_user_profile, generate_summary
from aws_dev_tracker.progress_logic import track_services, service_summary, add_certification

# Initialize user
user = get_user_profile("Charles", 2, "AWS Developer")

# Print profile summary
print(generate_summary(user))

# Update certification count
user["certifications"] = add_certification(user["certifications"])

# Print updated summary
print("\nUpdated Profile:")
print(generate_summary(user))

# List services
services = track_services()
print("\n" + service_summary(services))