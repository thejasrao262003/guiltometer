# 📅 Guiltometer - Week 6 README

## 🔁 Week 6 Focus: Agent Memory, Historical Trends & Final Polish

This week is about enhancing intelligence, improving user experience, and preparing for future extensibility. You’ll:
- Add memory to agents so they build on past data
- Track long-term consistency and trends
- Polish API responses and testing

---

## ✅ Goals for Week 6

---

### 1. 🧠 Agent Memory (Lightweight Implementation)

#### Purpose:
Allow agents to:
- Remember which topics were already suggested
- Avoid repeating advice
- Track overall task tone/effort week-over-week

#### Strategy:
- Use a `memory` field or a `history` table per agent:
  - Store last roadmap
  - Store previous recommendations
  - Store tone trend across weeks

#### Example:
```json
{
  "task_id": 1,
  "past_roadmaps": ["Sliding Window", "Binary Search"],
  "mood_trend": ["neutral", "positive", "negative"],
  "avg_focus_score": 3.8
}
```

#### Tasks:
- [ ] Update `roadmaps` to include topic history
- [ ] Agents pull this history during generation
- [ ] Store "agent memory" as embedded JSON or in separate table

---

### 2. 📊 Historical Trends Dashboard API

#### New Endpoints:
- GET `/analytics/{task_id}/consistency`  
  → returns % of days completed, streaks, drop-offs
- GET `/analytics/{task_id}/tone`  
  → returns mood changes over weeks
- GET `/analytics/{task_id}/score-history`  
  → guilt scores over time

---

### 3. ✅ API Response Polish & Documentation

- [ ] Add response models for all endpoints
- [ ] Return standardized JSON: `{ success: true, data: {...} }`
- [ ] Create minimal `docs.md` with all routes and examples
- [ ] Enable FastAPI Swagger at `/docs`

---

### 4. 🧪 Testing & Final Checks

- [ ] Add or expand test coverage for:
  - Tasks
  - Logs
  - Agents (mock Gemini calls)
- [ ] Ensure email/report generation works for test user
- [ ] Check weekly cron trigger (manual if needed)

---

## 📦 Optional Extras (If time permits)

- UI placeholder endpoint: `/me/dashboard` returning all task + log + roadmap
- Export to PDF using `pdfkit` or `WeasyPrint`
- Schedule weekly job using `cron` on EC2 or `cron-job.org`

---

## 📌 Output by End of Week

- [ ] Agents now consider past suggestions
- [ ] Historical analytics endpoints live
- [ ] Final test coverage in place
- [ ] API standardized and documented
- [ ] Deployment is stable and secure

---

## ⏳ Time Estimate
~8–10 hours  
→ Enough to polish, stabilize, and scale up later

---

Once done, you'll have a complete solo SaaS-style project that:
- Uses agents + LLMs to help you grow
- Runs in production
- Can be demoed, written about, or extended with mobile UI

Ready to build like a 10x engineer 🔥
