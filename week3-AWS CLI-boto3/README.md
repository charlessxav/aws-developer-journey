# Week 3 · Day 1 — AWS CLI Setup & S3 Basics (Free Tier)

**Flow:** **Revision → Hands-on → MCQ Quiz**  
**Outcome:** Install & configure AWS CLI v2, verify identity, create/use/clean up an S3 bucket — all **within AWS Free Tier**.

---

## 🎯 Objectives
- Install **AWS CLI v2** and configure credentials
- Verify identity with **STS**
- Create, list, upload, download, and delete **S3** objects/buckets
- Practice strict **cleanup** to avoid costs

---

## 🛡 Free Tier Guardrails
- Use **tiny test files** (<1KB) and keep total S3 usage well under **5 GB**.
- No paid storage classes (stick to **Standard**).
- Delete objects and buckets when finished.
- Use a single region (e.g., **us-east-1**) to avoid surprises.

---

## 🛠 Prerequisites (Free & Required)
1) **AWS Account** (root only for initial IAM setup)  
2) **IAM User (Programmatic access)** with temporary `AmazonS3FullAccess` (we’ll narrow later)  
3) **AWS CLI v2 installed**  
   - Install guide: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html  
4) **Default Region:** `us-east-1` (or nearest low-latency region)  
5) **Default Output:** `json`

---

## 🔄 Quick Revision (from Week 2)
- **JSON**: You’ll parse/emit JSON; great for scripts.
- **File I/O**: You’ll upload/download small files.
- **Error handling**: Read CLI errors carefully; they’re very descriptive.

---

## ▶️ Hands-on (Copy/Paste Friendly)

> Replace `<BUCKET>` with a **globally unique** name (e.g., `charles-w3d1-2025-08-15`).

### 1) Verify install
```bash
aws --version
```
**Expected:** `aws-cli/2.x.x Python/3.x.x ...`

### 2) Configure credentials
```bash
aws configure
# AWS Access Key ID: AKIA... 
# AWS Secret Access Key: ****************
# Default region name: us-east-1
# Default output format: json
```

### 3) Verify identity (STS)
```bash
aws sts get-caller-identity
```
**Expected JSON:**
```json
{
  "UserId": "AIDAEXAMPLEID",
  "Account": "123456789012",
  "Arn": "arn:aws:iam::123456789012:user/cli-user"
}
```

### 4) Create S3 bucket (Free Tier-safe)
```bash
aws s3 mb s3://<BUCKET> --region us-east-1
```
**Expected:**
```
make_bucket: <BUCKET>
```

### 5) Upload a tiny file
```bash
echo "Hello AWS S3" > hello.txt
aws s3 cp hello.txt s3://<BUCKET>/
```
**Expected:**
```
upload: ./hello.txt to s3://<BUCKET>/hello.txt
```

### 6) List bucket objects
```bash
aws s3 ls s3://<BUCKET>/
```
**Expected (example):**
```
2025-08-15  15:40:22         14 hello.txt
```

### 7) Download & verify
```bash
aws s3 cp s3://<BUCKET>/hello.txt downloaded_hello.txt
cat downloaded_hello.txt
```
**Expected:**
```
Hello AWS S3
```

### 8) Cleanup (must-do)
```bash
aws s3 rm s3://<BUCKET>/hello.txt
aws s3 rb s3://<BUCKET>
```
**Expected:**
```
delete: s3://<BUCKET>/hello.txt
remove_bucket: <BUCKET>
```

---

## 🧪 MCQ Quiz (You already aced this ✅)
10 questions on AWS CLI & S3 basics. If needed, retake anytime.

---

## 🧹 Troubleshooting
- **AccessDenied** → Check IAM permissions/profile.
- **BucketAlreadyExists** → Use a more unique bucket name.
- **ExpiredToken** → Re-run `aws configure` to refresh keys.
- **EndpointConnectionError** → Confirm region and network access.

---

## 🧭 What’s Next (Day 2)
- Install **boto3**
- Create an S3 bucket and upload files **programmatically** with Python
- Add error handling & cleanup script

---

## 🏗 Repo Structure
```
week-3/
└── day-1-aws-cli-s3/
    └── README.md
```

---

## 🧾 Commit Message
```
docs: add Week 3 Day 1 AWS CLI & S3 hands-on (free tier) with steps and cleanup
```
