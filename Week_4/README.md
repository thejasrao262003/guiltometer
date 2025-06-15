# 📅 Guiltometer - Week 4 README

## 🧠 Week 4 Focus: Weekly Guilt Report Agent + Roadmap Generator Agent

This week is the turning point where the system becomes intelligent on a weekly level. You’ll implement:
- The **Guilt Report Agent**: reflects on a week's progress
- The **Roadmap Generator Agent**: suggests a personalized plan for the next 7 days

---

## ✅ Goals for Week 4

### 1. 🧾 Guilt Report Generator Agent

#### Purpose:
Every **Saturday night**, this agent:
- Aggregates all logs for each task
- Analyzes trends, drop-offs, tone
- Assigns a **Guilt Score (0–100)** based on effort vs. intention
- Generates a reflection report (markdown + plain text)

#### Input:
```json
{
  "task_id": 1,
  "week_logs": [
    {"date": "2025-06-17", "metrics": {"focus": 3}, "note": "..."},
    ...
  ]
}
```

#### Output:
```json
{
  "guilt_score": 64,
  "summary": "You were consistent until Thursday but dipped...",
  "recommendation": "Try reducing workload on Fridays.",
  "mood_trend": "Neutral → Negative → Slightly Positive"
}
```

#### Task:
- [ ] Aggregate weekly logs
- [ ] Analyze using Gemini agent
- [ ] Save report to `weekly_reports` table
- [ ] Send report via email using markdown formatting

---

### 2. 🧭 Roadmap Generator Agent (Optional per task)

#### Purpose:
For roadmap-enabled tasks, generate a 7-day roadmap:
- Based on current progress, task category, previous topics
- Suggests **daily micro-goals** or topics

#### Input:
```json
{
  "task_name": "DSA Prep",
  "logs": [...],
  "goal_progress": "Arrays, Prefix Sums done"
}
```

#### Output:
```json
{
  "week_plan": [
    {"day": "Monday", "task": "Sliding Window - 2 problems"},
    {"day": "Tuesday", "task": "Binary Search"},
    ...
  ],
  "theme": "Improve Pattern Recognition",
  "estimated_time": "6 hours"
}
```

#### Task:
- [ ] Agent recommends next steps from a topic graph or heuristics
- [ ] Output stored in `roadmaps` table
- [ ] Attach roadmap to email report

---

## 🛠 Agent Prompt Suggestions

- Guilt Score = Weighted score based on consistency, reflection tone, target match
- Roadmap generation = Curriculum heuristics or prompt chain like:
  - “What’s the next 3 subtopics after arrays for a beginner in DSA?”

---

## 🧪 Testing Strategy

- [ ] Manually trigger agents via script (`scripts/schedule_tasks.py`)
- [ ] Test on fake logs with different behavior patterns
- [ ] Check generated guilt report + roadmap JSON output
- [ ] Ensure markdown → email conversion looks clean

---

## 📂 Suggested Files

```
app/
├── agents/
│   ├── guilt_report.py
│   └── roadmap_generator.py
├── scripts/
│   └── schedule_tasks.py  # Run weekly via cron or manual
├── services/
│   └── email_service.py
```

---

## 📧 Email Format Example

Subject: `"📊 Guiltometer Weekly Report – DSA Prep"`

```
## Summary
You completed 4 out of 5 days. Great job!

## Guilt Score
🟡 64 / 100

## Weekly Mood Trend
🙂 → 😐 → 😞

## Suggestions
- Skip heavy topics on Thursday
- Break large goals into smaller parts

## Roadmap for Next Week
- Mon: Sliding Window
- Tue: Binary Search
...
```

---

## 📌 Output by End of Week

- [ ] Working guilt report agent
- [ ] Roadmap generator agent (at least DSA-focused)
- [ ] Email service sending markdown reports
- [ ] Script for triggering weekly flow

---

## ⏳ Time Estimate
~10–12 hours total  
→ Stretch task, so balance agent writing and email/report testing on the weekend.

---

Coming up next: **Week 5 – DevOps + Cloud Deployment (Docker + GitHub Actions + Hosting)**.
