# 🗂️ Week 2 – Functions, Files, JSON & Error Handling

This folder contains hands-on work, code challenges, and quizzes from **Week 2** of my AWS Developer Learning Journey.

---

## 📅 Topics Covered

- Python function definition, parameters, and return values
- Default arguments & modular coding
- File reading/writing with `.txt` files
- JSON parsing and manipulation in Python
- Exception handling using `try`/`except`
- Small CLI-style automation projects

---

## 🗂️ Folder Structure (Week 2)

```
week2-functions-files-json/
├── week2_functions_basics.py              # Day 1
├── day2_parameters_modules.py             # Day 2 (main script)
├── greetings_module.py                    # Day 2 (helper module)
├── math_utils.py                          # Day 2 (optional helper)
├── (upcoming) day3_file_io.py             # Day 3
├── (upcoming) day4_json_parsing.py        # Day 4
├── (upcoming) day5_error_handling.py      # Day 5
└── README.md
```

> Files with **(upcoming)** will be added as the week progresses.

---

## 📝 Day-by-Day Breakdown

| Day   | Topic/Challenge                               | File Name(s)                           | Status |
|-------|-----------------------------------------------|----------------------------------------|--------|
| Day 1 | Function basics: define, call, return         | `week2_functions_basics.py`            | ✅ Done |
| Day 2 | Parameters, default args, modules             | `day2_parameters_modules.py`, `greetings_module.py`, `math_utils.py` | 🔄 In progress |
| Day 3 | File I/O: reading & writing                   | `(upcoming) day3_file_io.py`           | ⏳     |
| Day 4 | JSON parsing: load/save, hands-on             | `(upcoming) day4_json_parsing.py`      | ⏳     |
| Day 5 | Error handling: try/except, challenge         | `(upcoming) day5_error_handling.py`    | ⏳     |
| Day 6 | Quiz + Build: Config loader tool              | `(upcoming)`                           | ⏳     |

---

## 🧪 Mini Project (Week 1–2 So Far): AWS Developer CLI Tracker

A modular CLI-style tool that tracks user profile and AWS learning progress.

**Planned files (live under this week’s folder):**
- `aws_dev_tracker/user_profile.py` – build a profile dict (`name`, `goal`, `certifications`)
- `aws_dev_tracker/progress_logic.py` – list services, format summaries, add certification
- `main.py` – entry point that prints the progress summary

**Planned output:**

```
Charles is learning AWS to become a AWS Developer.
Certifications: 2

[Updated Profile]
Charles is learning AWS to become a AWS Developer.
Certifications: 3

Learning AWS services:
- S3
- Lambda
- CloudWatch
- DynamoDB
- CloudFormation
```

> I’m coding this myself to reinforce fundamentals; the structure/algorithm is documented above.

---

## ▶️ How to Run

From repo root (or from this folder):

```bash
# Day 1 example
python week2-functions-files-json/week2_functions_basics.py

# Day 2 example
python week2-functions-files-json/day2_parameters_modules.py
```

---

## 🚀 Sample Snippets (from this week)

```python
def greet(name):
    print(f"Welcome, {name}! Ready for AWS?")

def add_certifications(current, new=1):
    return current + new
```

---

## ✅ Progress Checklist (Week 2)

- [x] Day 1 – Functions: define/call/return
- [ ] Day 2 – Parameters, defaults, modules
- [ ] Day 3 – File I/O
- [ ] Day 4 – JSON parsing
- [ ] Day 5 – Error handling
- [ ] Day 6 – Quiz + Config loader mini build

---

## 💡 How This Connects to AWS

- Functions & modules → **Lambda handlers / helper libs**
- File I/O & JSON → **config, payloads, IAM policies**
- Error handling → **reliable automation scripts**
- CLI patterns → **boto3-based tooling**

---

## 🏷️ Tags

`#python` `#functions` `#modules` `#aws` `#automation` `#learning-journey`

---

> Week 2 builds the foundation for AWS SDK (boto3), serverless apps, and IaC.