import json

# Example AWS Learning profile
aws_profile = {
    "name": "Charles",
    "goal": "AWS Developer",
    "certifications" : 2,
    "learning" : True,
    "services" : ["S3", "Lambda", "Cloudwatch"]
}

# Save profile to a JSON file
with open("aws_profile.json", "w") as file:
    json.dump(aws_profile, file, indent=4)
    print("JSON file created successfully.")
    
# Load profile from the JSON file
with open("aws_profile.json", "r") as file:
    loaded_profile = json.load(file)

# Print the loaded profile
print("Loaded AWS Profile:", loaded_profile)

# Modify the JSON data
loaded_profile["services"].append("DynamoDB")

# Save appended data back to the JSON file
with open("aws_profile.json", "w") as file:
    json.dump(loaded_profile, file, indent=4)
    print("Profile updated successfully.")

#Print the updated profile
print("Updated AWS Profile:", loaded_profile)