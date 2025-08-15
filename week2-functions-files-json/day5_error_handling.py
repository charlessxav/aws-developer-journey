import json

# Try loading a JSON file that may not exist
try:
    with open("aws_profile.json", "r") as file:
        profile = json.load(file)
    print("AWS Profile loaded successfully.", profile)

except FileNotFoundError:
    print("Error: The file 'aws_profile.json' was not found. Please run Day 4 first")

except json.JSONDecodeError:
    print("Error: 'aws_profile.jsob' is not a valid JSON file.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")  

finally:
    print("Execution completed successfully.")

