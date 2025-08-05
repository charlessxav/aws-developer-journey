profile = {
    "name": "Charles",
    "certifications": 1,
    "learning": True,
    "favorite_service": "S3",
    "days_per_week": 6
}

profile["goal_role"] = "AWS Developer"
profile["favorite_service"] = "Lambda"

for key,value in profile.items():
    print(f"{key} -> {value}")