def build_profile(name, role, certified):
    status = "✅ Certified" if certified else "🚧 Not Certified"
    return f"{name} is learning AWS to become a {role}. \nStatus: {status}"

output = build_profile("Charles", "Developer", True)
print(output)