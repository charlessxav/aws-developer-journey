certified_input = input("Are you AWS Certified? (yes/no): ")

#Normalize input
certified = certified_input.lower() == "yes"

#Logic Checks
if certified:
    # Get years of experience
    experience = int(input("Years of experience: "))
    if experience >= 2:
        # Get learning path
        path = input("Learning path (developer/architect): ")
        if path == "developer":
            print("✅ Ready for AWS Developer role!")
        elif path == "architect":
            print("✅ Ready for AWS Architect role!")   
        else:
            print("🚧 Unknown path, please enter 'developer' or 'architect'.")    
    else:
        print("🔄 Keep building experience.")
else:
    print("🚧 Complete your certification first.")