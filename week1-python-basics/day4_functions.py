def introduce_yourself():
    print("My name is Charles.\nI am learning AWS to become a Developer.")

introduce_yourself()

def aws_goal(name, role):
    print(f"{name} is preparing for the AWS {role} role.")

aws_goal("Charles", "Developer" )

def get_certification_status():
    return True
is_certified = get_certification_status()
print(f"Certified: {is_certified}")