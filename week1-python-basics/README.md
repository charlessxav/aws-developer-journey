# 🐍 Day 1 – Python Basics for AWS

This script demonstrates the fundamentals of Python — the core language you'll use in AWS automation, Lambda functions, and backend scripts.

## ✅ Topics Covered
- Variables (`str`, `int`, `bool`)
- f-strings for string formatting
- `print()` for output
- `type()` to inspect data types
- Running Python scripts in VS Code

## 📁 File
- `day1_intro.py` — contains your first Python script

## 📌 Example Output

```
My name is Charles. I like AWS S3. I have 1 certifications. Learning AWS: True
<class 'str'>
<class 'str'>
<class 'int'>
<class 'bool'>
```

## 🚀 Next Step
👉 Day 2: Lists & Dictionaries

---

> 💡 This is part of a full 14-week AWS Developer Learning Path.


---

# 🧩 Day 2 – Python Collections: Lists & Dictionaries

Learned how to use Python's most important data structures for AWS scripting:
- Lists: Ordered collections for EC2 IDs, services, etc.
- Dictionaries: Key-value pairs used in configs, tags, payloads

## ✅ Topics Covered
### Lists:
- Creating and modifying lists
- Appending and removing items
- Looping with `for` loops
- Real-world use: managing AWS service names dynamically

### Dictionaries:
- Creating key-value pairs
- Accessing, updating, and deleting keys
- Looping through dictionaries with `.items()`
- Real-world use: Lambda payloads, tagging, config files

## 📁 Files
- `day2_collections.py` — List operations and looping
- `day2_dict_profile.py` — AWS learning profile using a dictionary

## 📌 Example Output

```
Learning AWS services:
- S3
- Lambda
- Cloudwatch
- DynamoDB
- CloudFormation

name -> Charles
certifications -> 1
learning -> True
favorite_service -> Lambda
days_per_week -> 6
goal_role -> AWS Developer
```

## 🧠 Summary
These structures are foundational for writing real AWS automation scripts and working with APIs like `boto3`.

---

> 💡 Part of a full 14-week AWS Developer Learning Path.