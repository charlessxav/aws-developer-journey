certified_input = input("Are you AWS certified? (yes/no): ")
experience_years = int(input("Years of experience: "))
learning_path = input("Learning path (developer/architect): ")

certified = certified_input.lower() == "yes"

if certified and learning_path == "developer":
    print("✅ Ready for AWS Developer role!")
elif certified and experience_years <= 2:
    print("🔄 Keep building experience.")
else:
    print("🚧 Complete your certification first.")

