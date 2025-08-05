week_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"
             ]
for days in week_days:
    print(f"Study Plan for: {days}")


day = 1
while day <= 5:
    print(f"Day {day} of learning")
    day += 1

services = {
    "S3": "Storage",
    "Lambda": "Compute",
    "Cloudwatch": "Monitoring"
}

for key, value in services.items():
    print(f"{key} is used for: {value}")

    