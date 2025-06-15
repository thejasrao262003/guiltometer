# 📅 Guiltometer - Week 3 README

## 🧠 Week 3 Focus: Agentic Framework Integration – Goal Architect & Daily Log Interpreter

This week, you’ll begin integrating **LLM agents** using Gemini to intelligently interpret and support user behavior. You'll implement the **Goal Architect Agent** (to auto-structure tasks) and the **Daily Log Interpreter Agent** (to analyze daily logs).

---

## ✅ Goals for Week 3

### 1. 🤖 Integrate LangChain + Gemini

#### 📦 Setup
- [ ] Install `langchain`, `google-generativeai`
- [ ] Set up Gemini API key using `google.generativeai`
- [ ] Create a LangChain wrapper to call Gemini
- [ ] Optional: Use `CrewAI` or `AgentOps` to manage agents (basic wrapper works fine for now)

---

### 2. 🧠 Goal Architect Agent

#### Purpose:
When a user creates a new task (e.g., `"Get better at DSA"`), this agent:
- Refines goal name
- Categorizes the task (e.g., Career, Discipline, Health)
- Suggests metrics (e.g., focus, time_spent, consistency)
- Optionally: suggests a roadmap structure (stored later)

#### Input:
```json
{
  "name": "Workout regularly",
  "description": "Build stamina and lose fat",
  "roadmap_enabled": true
}
```

#### Output:
```json
{
  "refined_name": "Daily Cardio Workout",
  "category": "Health",
  "metrics": ["duration", "intensity", "mood"],
  "default_frequency": 5
}
```

#### Task:
- [ ] Build this agent as a function callable on task creation
- [ ] Store its output in `tasks` table
- [ ] Fallback to defaults if Gemini call fails

---

### 3. ✍️ Daily Log Interpreter Agent

#### Purpose:
Every night (or post-log), this agent:
- Interprets user's notes/mood
- Detects drop in effort or tone
- Fills missing metric estimates (if user didn’t input all fields)

#### Input:
```json
{
  "metrics": {
    "focus": 3,
    "mood": "meh"
  },
  "note": "Didn't feel like doing much"
}
```

#### Output:
```json
{
  "emotion_score": -1,
  "auto_notes": "Detected fatigue, recommend reducing load tomorrow",
  "fill_ins": {"duration": 0}
}
```

#### Task:
- [ ] Trigger this agent post log submission
- [ ] Store insights in a `log_analysis` table or append to `logs`
- [ ] Allow agent to enrich log with reflection insights

---

## 🧪 Testing Strategy

- Manually test Gemini calls via FastAPI endpoints
- Write test logs with emotional/mood variation
- Validate correct generation of:
  - task structuring
  - log enrichment

---

## 📌 Output by End of Week

- [ ] Working LangChain Gemini wrapper
- [ ] Architect agent enhancing `/tasks/` flow
- [ ] Daily log interpreter triggered after `/logs/` submission
- [ ] Schema update: Add optional `analysis` field to logs

---

## 🛠 Folder Suggestions

```
app/
├── agents/
│   ├── goal_architect.py
│   └── log_interpreter.py
├── services/
│   └── gemini_wrapper.py
```

---

## 🧠 Design Notes

- Each agent should be modular and stateless
- If an agent fails, log it but allow the app to continue
- Use structured prompt templates, stored in code or markdown

---

## ⏳ Time Estimate
~9–11 hours total  
→ 1.5 hours on weekdays, deep dive on weekend

---

Up next: **Week 4 – Weekly Guilt Report Agent + Roadmap Generator** (your first scheduled agent flows).
