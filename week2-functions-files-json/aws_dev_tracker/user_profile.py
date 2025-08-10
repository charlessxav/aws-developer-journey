def get_user_profile(name="Charles", certs=1, goal="AWS Developer"):

    return {
        "name": name,
        "certifications": certs,
        "goal": goal        
    }


def generate_summary(profile):
    
    return f"{profile['name']}, is learning AWS to become a {profile['goal']}.Certifications: {profile['certifications']}"