
# Week 3 · Day 2 — boto3 S3 (Two-file variant: `sample1.txt` & `sample2.txt` at repo root)

You updated your Day 2 script to handle **two input files** and placed them at the **repo root** so Python can find them easily.
This README reflects that setup while keeping everything **AWS Free Tier** safe.

---

## 🎯 What this does
- Creates a **unique S3 bucket** (UUID-suffixed) in your chosen region
- **Uploads two files**: `sample1.txt` and `sample2.txt` (from repo root)
- **Lists** the objects to verify both uploads
- **Downloads** the objects (your script’s filenames/paths)
- **Cleans up** (deletes objects + bucket) to avoid costs

---

## 📁 Repo Layout (your current approach)
```
<repo-root>/
├── sample1.txt
├── sample2.txt
└── week-3/
    └── day-2-boto3-s3/
        └── day2_s3_boto3.py   # your two-file version
```

> Keep `sample1.txt` and `sample2.txt` **tiny** (a few bytes). Example contents:
> - `sample1.txt`: `Hello from sample1!`
> - `sample2.txt`: `Hello from sample2!`

---

## 🛠 Prerequisites
- Week 3 Day 1 done (AWS CLI configured; IAM user ready)
- Python **3.10+**
- `boto3` installed:
  ```bash
  pip install boto3
  ```

---

## ▶️ How to Run (from repo root)
Run your script from the **repo root** so relative paths to `sample1.txt` and `sample2.txt` resolve correctly:
```bash
python week-3/day-2-boto3-s3/day2_s3_boto3.py
```
*(If your script supports CLI flags for filenames, you can pass them. Otherwise it should pick up `sample1.txt` and `sample2.txt` from root as you implemented.)*

---

## ✅ Expected Flow / Output (example)
```
Region       : us-east-1
Bucket (new) : charles-w3d2-a1b2c3d4

== Upload files ==
✅ Uploaded: sample1.txt -> s3://charles-w3d2-a1b2c3d4/sample1.txt
✅ Uploaded: sample2.txt -> s3://charles-w3d2-a1b2c3d4/sample2.txt

== List objects ==
Objects: ['sample1.txt', 'sample2.txt']

== Download files ==
✅ Downloaded: sample1.txt  -> downloaded_sample1.txt   # (or whatever your code uses)
✅ Downloaded: sample2.txt  -> downloaded_sample2.txt   # (or whatever your code uses)

== Cleanup (objects + bucket) ==
✅ Deleted: s3://charles-w3d2-a1b2c3d4/sample1.txt
✅ Deleted: s3://charles-w3d2-a1b2c3d4/sample2.txt
✅ Bucket removed: charles-w3d2-a1b2c3d4
```

> If you see `BucketAlreadyExists` or `BucketAlreadyOwnedByYou`, just rerun (your UUID-suffixed name will change).
> If you cancel mid-run, re-run once to let cleanup finish, or delete via AWS Console/CLI.

---

## 🧹 Free Tier Guardrails
- Keep files **tiny** and delete everything at the end (script already does).
- Stick to a single region (e.g., `us-east-1`) for predictable behavior.
- Never upload large files; we only need a few bytes for learning.

---

## 🧾 Commit Message
```
docs: update Week 3 Day 2 README for two-file S3 upload (sample1 & sample2 at repo root)
```

---

## 🧭 Next (Day 3)
boto3 + EC2 (Free Tier): list, start, stop **t2.micro/t3.micro** with strict cleanup and safety checks.