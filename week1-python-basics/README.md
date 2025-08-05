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

---

# 🔁 Day 3 – Python Control Flow

Learned how to use `if`, `else`, and `elif` to control program behavior. Practiced building real-world logic used in AWS scripts and automations.

## ✅ Topics Covered
- `if`, `elif`, `else` decision-making
- Logical operators: `and`, `or`, `not`
- Nested conditions
- User input via `input()`
- Real-world logic: role-readiness based on certs, experience, and path

## 📁 Files
- `day3_conditions.py` — basic role evaluation with logic
- `day3_input_conditions.py` — interactive version with user input and nested checks

## 📌 Example Output

```
Are you AWS certified? (yes/no): yes
Years of experience: 3
Learning path (developer/architect): developer
✅ Ready for AWS Developer role!
```

---

# 🧮 Day 4 – Python Functions & Reusability

Learned how to write reusable, modular code using functions — the building block of all automation and AWS Lambda scripts.

## ✅ Topics Covered
- Defining functions with `def`
- Passing arguments (parameters)
- Using `return` for reusable logic
- Function composition
- Input + logic + output formatting

## 📁 Files
- `day4_functions.py` — multiple functions: greet, goals, cert status
- `day4_profile_builder.py` — combined challenge with return + logic

## 📌 Example Output

```
Charles is learning AWS to become a Developer.
Status: ✅ Certified
```

---

# 🔁 Day 5 – Python Loops: Lists, Counters, Dictionaries

Learned how to repeat logic over sequences — critical for working with AWS resources, files, and repetitive actions.

## ✅ Topics Covered
- `for` loops over lists
- `while` loops with conditions
- Looping through dictionaries using `.items()`
- Counting with `range()` and formatted output

## 📁 File
- `day5_loops.py` — printed weekdays, counted learning days, iterated AWS service dictionary

## 📌 Example Output

```
Study Plan for: Mon
Study Plan for: Tue
...
Day 1 of learning
Day 2 of learning
...
S3 is used for: Storage
Lambda is used for: Compute
Cloudwatch is used for: Monitoring
```

---

> 💡 You’ve completed Week 1 of the 14-week AWS Developer journey!