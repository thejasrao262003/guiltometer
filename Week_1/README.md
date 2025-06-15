# 📅 Guiltometer - Week 1 README

## 🧠 Week 1 Focus: Project Setup & Database Design

This week is about getting the foundational backend ready. The goal is to prepare the FastAPI app structure and define the database schema for tasks, logs, and reports.

---

## ✅ Goals for Week 1

### 1. 🔧 FastAPI Project Bootstrap
- [ ] Create virtual environment and install `fastapi`, `uvicorn`, `sqlalchemy`, `psycopg2-binary`, `alembic`
- [ ] Scaffold the project:
  ```
  app/
    ├── main.py
    ├── models/
    ├── routers/
    ├── services/
    └── agents/
  ```

### 2. 🗃️ PostgreSQL Schema Design
Define and create the following tables using SQLAlchemy or Alembic:

#### 📌 `users`
- id (UUID)
- email
- api_key (TEXT) ← personal Gemini API key for each user
- created_at

#### 📌 `tasks`
- id
- user_id (FK)
- name
- category
- start_date
- target_frequency (nullable)
- expected_duration_days (nullable)
- roadmap_enabled (bool)
- created_at

#### 📌 `daily_logs`
- id
- task_id (FK)
- date
- metrics (JSONB: {"focus": 4, "mood": "meh"})
- note (optional)
- created_at

#### 📌 `weekly_reports`
- id
- task_id (FK)
- week_start_date
- guilt_score (int)
- analysis (TEXT)
- created_at

#### 📌 `roadmaps`
- id
- task_id (FK)
- week_start_date
- roadmap_json (JSONB)
- created_at

### 3. 🔄 Database Setup
- [ ] Create local PostgreSQL DB
- [ ] Create tables via Alembic or SQLAlchemy
- [ ] Seed test user + task for local dev

---

## 🧪 Testing
- [ ] Launch FastAPI with `uvicorn app.main:app --reload`
- [ ] Test DB connection
- [ ] Ensure all models and basic queries work

---

## 🛠️ Tools
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic (for migrations)
- Python 3.11+

---

## 📌 Output by End of Week
- [ ] Working FastAPI app running locally
- [ ] PostgreSQL schema defined and running
- [ ] Test data inserted and verified via simple query

---

## ⏳ Time Estimate
~6–8 hours total  
→ ~1–1.5 hours x 5 weekdays = manageable

---
