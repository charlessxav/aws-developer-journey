# 🗂️ Week 2 – Functions, Files, JSON & Error Handling

This folder contains all hands-on work, code challenges, and quizzes from **Week 2** of my AWS Developer Learning Journey.

---

## 📅 Topics Covered

- Python function definition, parameters, and return values  
- Positional, keyword, and default arguments  
- Organizing code with Python modules  
- File reading/writing with `.txt` files  
- JSON parsing and manipulation in Python  
- Exception handling using `try`/`except`  
- CLI and small automation projects  

---

## 📝 Day-by-Day Breakdown

| Day   | Topic/Challenge                                 | File Name(s)                      |
|-------|-------------------------------------------------|------------------------------------|
| Day 1 | Function basics: define, call, return           | `week2_functions_basics.py`       |
| Day 2 | Parameters, default args, modules               | `day2_parameters_modules.py`, `greetings_module.py`, `math_utils.py` |
| Day 3 | File I/O: reading & writing                     | `day3_file_io.py`                  |
| Day 4 | JSON parsing: load/save, hands-on                | `day4_json_parsing.py`             |
| Day 5 | Error handling: try/except, challenge            | `day5_error_handling.py`            |
| Day 6 | **Revision + Mini-Project + MCQ Quiz**           | `day6_config_loader.py`, `config.json` |

---

## 🚀 Sample Code (from this week)

```python
# greetings_module.py
def greet_user(name, role="Learner"):
    print(f"Hello {name}, you are learning to be an {role}!")

# math_utils.py
def add_numbers(a, b):
    return a + b

# day3_file_io.py
with open("study_plan.txt", "w") as file:
    file.write("Day 1 of Learning\n")
    file.write("Day 2 of Learning\n")
    file.write("Day 3 of Learning\n")

with open("study_plan.txt", "a") as file:
    file.write("Day 4 of Learning\n")

with open("study_plan.txt", "r") as file:
    content = file.read()
    print("📄 File Content:\n", content)

# day4_json_parsing.py
import json

aws_profile = {
    "name": "Charles",
    "goal": "AWS Developer",
    "certifications": 2,
    "learning": True,
    "services": ["S3", "Lambda", "CloudWatch"]
}

with open("aws_profile.json", "w") as file:
    json.dump(aws_profile, file, indent=4)

with open("aws_profile.json", "r") as file:
    loaded_profile = json.load(file)

loaded_profile["services"].append("DynamoDB")

with open("aws_profile.json", "w") as file:
    json.dump(loaded_profile, file, indent=4)
```

---

## 🎯 What I Learned

- Writing and organizing functions for reusability  
- Using positional, keyword, and default arguments effectively  
- Splitting code into modules for better maintainability  
- Reading/writing `.txt` files for automation  
- Parsing, modifying, and saving JSON data for AWS scripts  
- Handling file and JSON errors gracefully  

---

## 💡 How This Connects to AWS

These skills are directly relevant to:  
- Writing AWS Lambda functions with parameters  
- Structuring boto3 automation scripts  
- Creating modular AWS CLI tools  
- Saving AWS CLI output and loading configuration files in JSON  

---

## 📂 Mini-Projects This Week

### AWS Developer CLI Tracker
**Goal:** Build a command-line tool to manage AWS learning progress.  

**Features:**
- Store & display AWS learning profile (name, role, certifications, services)  
- Add new AWS services to your learning list  
- Generate summaries using f-strings  
- Use parameters and modules for organized, reusable code  
- Save/load progress from text or JSON files  

---

### Day 6 – Config Loader Tool
**Goal:** Load configuration from a JSON file, validate required keys, and display them neatly.  

**Files:**  
- `config.json` – Sample config file  
- `day6_config_loader.py` – Main script  

**Key Features:**
- Uses **functions** to load, validate, and display config data  
- Handles missing files, bad JSON, or missing keys  
- Prints output in a clean, recruiter-friendly way  

**Example Output:**
```
=== Application Configuration ===
app_name: MyAWSApp
version: 1.0
debug: True
max_connections: 5
Config loader finished.
```

---

## 🧩 Day 6 MCQ Quiz

A 10-question multiple choice quiz covering **Functions, Parameters, Modules, File I/O, JSON, and Error Handling** to reinforce the week’s learning.

---

## 🏷️ Tags

`#python` `#functions` `#modules` `#file-io` `#json` `#aws` `#automation` `#portfolio`

---

> This week is part of a structured 14-week AWS Developer portfolio journey.