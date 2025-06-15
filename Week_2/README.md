# 📅 Guiltometer - Week 2 README

## 🧠 Week 2 Focus: Daily Logging System & Task Management API

This week is about building the **core APIs** that allow users to:
- Create and manage goals/tasks
- Log daily progress
- Retrieve logs and task details

---

## ✅ Goals for Week 2

### 1. 🚧 Task Management Endpoints

#### ✅ POST `/tasks/`
- **Purpose**: Create a new goal/task
- **Request**:
```json
{
  "name": "DSA Prep",
  "category": "Career",
  "start_date": "2025-06-17",
  "target_frequency": 5,
  "expected_duration_days": 60,
  "roadmap_enabled": true
}
```

- **Response**:
```json
{
  "id": 1,
  "message": "Task created successfully"
}
```

#### ✅ GET `/tasks/`
- **Purpose**: List all active tasks for the user

#### ✅ GET `/tasks/{id}`
- **Purpose**: Fetch a specific task and its metadata

#### ✅ DELETE `/tasks/{id}`
- **Purpose**: Archive/delete a task

---

### 2. 🗓️ Daily Logging Endpoints

#### ✅ POST `/logs/`
- **Purpose**: Log daily metrics for a task
- **Request**:
```json
{
  "task_id": 1,
  "date": "2025-06-18",
  "metrics": {
    "focus": 4,
    "duration": 60,
    "mood": "neutral"
  },
  "note": "Did some binary search problems"
}
```

- **Response**:
```json
{
  "message": "Log saved successfully"
}
```

#### ✅ GET `/logs/{task_id}?start=YYYY-MM-DD&end=YYYY-MM-DD`
- **Purpose**: Fetch logs for a specific task between given dates

---

## 🔐 Auth Layer

- For now, add **JWT-based auth** using `fastapi-users` or a simple dependency override
- Each user should only access their own tasks and logs

---

## 🧪 Testing Suggestions

- Use **Postman** or **Thunder Client** in VS Code
- Simulate:
  - Creating a task
  - Logging data for multiple days
  - Fetching task and log history

---

## 🛠️ Recommended Folder Structure Additions

```
app/
├── routers/
│   ├── tasks.py         # All /tasks endpoints
│   └── logs.py          # All /logs endpoints
├── models/
│   ├── task.py
│   └── log.py
├── schemas/
│   ├── task_schema.py   # Pydantic models
│   └── log_schema.py
├── services/
│   ├── task_service.py
│   └── log_service.py
```

---

## 📌 Output by End of Week

- [ ] Working CRUD API for tasks
- [ ] Working POST + GET APIs for daily logs
- [ ] Proper foreign key relationships tested
- [ ] Postman collection for testing all endpoints
- [ ] Auth layer (even basic) functional

---

## 🧠 Things to Keep in Mind

- Metrics are **dynamic per task**, so define a `JSONB` structure to store them flexibly
- Allow `note` to be optional
- Set sensible defaults (e.g., if date not provided, assume today)

---

## ⏳ Time Estimate
~8–10 hours total  
→ Ideal for 1–1.5 hrs/day plus weekend wrap-up/testing

---

Once you're done with this week, we'll move into **Week 3: Agents for Goal Structuring and Daily Log Interpretation** using LangChain + Gemini.

