# 📅 Guiltometer - Week 5 README

## 🛠️ Week 5 Focus: DevOps, Dockerization & Cloud Deployment

This week, you’ll productionize your backend:
- Dockerize the FastAPI app
- Add CI/CD with GitHub Actions
- Deploy to the cloud (Render, EC2, or Railway)
- Set up database backups and secure API keys

---

## ✅ Goals for Week 5

---

### 1. 🐳 Dockerize FastAPI App

#### Create `Dockerfile`
```Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### Create `.dockerignore`
```
__pycache__/
*.pyc
.env
tests/
```

#### Build & Run
```bash
docker build -t guiltometer-backend .
docker run -p 8000:8000 guiltometer-backend
```

---

### 2. ⚙️ CI/CD with GitHub Actions

#### Create `.github/workflows/ci.yml`
```yaml
name: Guiltometer CI

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      - name: Run Tests
        run: |
          pytest
```

> Add a `tests/` folder and at least one basic test to validate CI.

---

### 3. ☁️ Cloud Deployment Options

#### Option A: **Render**
- Connect GitHub repo
- Add environment variables
- PostgreSQL (hosted or managed)

#### Option B: **AWS EC2**
- Install Docker + Git
- Push Docker image
- Run with `docker run -d ...`
- Open port 8000 in security group

#### Option C: **Railway**
- Easiest DB + deploy in one place
- Auto CI from GitHub

---

### 4. 🔐 Secrets Management

- Use `.env` for:
  - DB URL
  - Gemini API Key
  - Email credentials
- Use `python-dotenv` or Render's built-in env manager
- Never push `.env` to GitHub

---

### 5. 🛡️ DB Backup Script (Optional)

#### Basic backup (PostgreSQL)
```bash
pg_dump -U youruser -h yourhost -d yourdb > backup.sql
```

#### Automate with cron (on EC2 or local)

---

## 📂 Suggested Files

```
project/
├── Dockerfile
├── .dockerignore
├── .env.example
├── .github/
│   └── workflows/
│       └── ci.yml
```

---

## 📌 Output by End of Week

- [ ] Dockerized FastAPI app
- [ ] CI workflow for builds + tests
- [ ] Deployed live API (Render, EC2, or Railway)
- [ ] Secure .env handling
- [ ] Optional: DB backup working

---

## ⏳ Time Estimate
~10–12 hours  
→ DevOps is heavier; allocate your weekend wisely.

---

Next week: **Final Polish + Agent Memory + Historical Trends**.
