# 🧠 Guiltometer: The Personal Growth Engine

Guiltometer is a solo-tracker that uses agentic LLMs to log, analyze, and improve your consistency across goals like DSA prep, fitness, writing, and more. Every Saturday, you get a Guilt Score and AI-generated Roadmap for the week ahead.

---

## 🔧 Tech Stack (Focus Areas)

- **Backend**: FastAPI, PostgreSQL
- **Agents**: LangChain / CrewAI
- **Cloud/DevOps**: Docker, GitHub Actions, AWS/Render, Supabase
- **Storage**: S3 or Supabase (for roadmap history/reports)
- **LLMs**: Gemini Pro via Google AI Studio (initially)

---

## 📦 Project Structure

```
guiltometer/
├── app/
│   ├── models/         # SQLAlchemy models
│   ├── routers/        # API endpoints
│   ├── agents/         # LangChain agents (Architect, Logger, Reporter)
│   ├── services/       # Email, report generation, roadmap planner
│   └── main.py         # FastAPI entry
├── scripts/
│   └── schedule_tasks.py  # Weekly cron tasks
├── tests/
│   └── ...             # Unit + API tests
├── docker/
│   └── Dockerfile
├── .github/
│   └── workflows/
│       └── ci.yml
└── README.md
```

---

## 🗓️ Weekly Goals

### ✅ Week 1 – Setup
- [ ] Initialize Git repo
- [ ] Set up FastAPI + SQLAlchemy + PostgreSQL
- [ ] Design schema: `users`, `tasks`, `logs`, `reports`, `roadmaps`

### ✅ Week 2 – Logging System
- [ ] Build API: create task, log data, get logs
- [ ] Auth: JWT or Supabase Auth
- [ ] Test logging flow with Postman

### ✅ Week 3 – Agent 1 & 2: Architect + Daily Interpreter
- [ ] Prompt template for goal breakdown
- [ ] Agent that tags goals, assigns metrics
- [ ] Agent that interprets mood/log entries

### ✅ Week 4 – Agent 3 & 4: Weekly Report + Roadmap Generator
- [ ] Generate guilt score & insights
- [ ] Build roadmap generator (per-task)
- [ ] Email + Markdown formatter for reports

### ✅ Week 5 – DevOps & Deployment
- [ ] Dockerize backend
- [ ] GitHub Actions: test + deploy
- [ ] Deploy to Render / EC2
- [ ] Backup DB (pg_dump)

### ✅ Week 6 – Polish & Memory
- [ ] Store roadmap history
- [ ] Refine agent memory (avoid repetition)
- [ ] Add tests for critical flows

---

## 📬 Weekly Deliverables

- **Saturdays**:
  - Guilt Report
  - AI-generated Roadmap (for selected goals)
- **Dashboard API (v1)**: `/goals`, `/logs`, `/roadmap`, `/report`

---

## 🚀 Future Enhancements

- Voice reflections → sentiment analysis
- Notion / Google Calendar sync
- Productivity score graphs
- Telegram reminders via bot

---
[User Stories](https://docs.google.com/spreadsheets/d/10L9mRiL6wwwBSIULxfnbVBYAgJmrwtWXiMflXBZyWOg/edit?usp=sharing)
---

## 🙌 Contribution

This is a solo project, but modular and agentic by design. You are the product, the user, and the builder.
