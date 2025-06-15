# 🖥️ Guiltometer Frontend README (Optional Integration Guide)

> This guide is for integrating a simple frontend interface with the Guiltometer backend. This is intentionally lightweight, since frontend is not a core focus for this project.

---

## 🎯 Goals

- Let user **create tasks**, **log daily progress**, and **view reports**
- Minimal UI with clean state handling and API integration
- Focus on **correct API wiring**, not fancy design

---

## 🧰 Recommended Tech Stack

- **Framework**: React (Vite or CRA)
- **Styling**: Tailwind CSS or plain CSS
- **Auth**: Supabase Auth or JWT handling via localStorage
- **State**: React Context API or Zustand

---

## 📦 Folder Structure

```
src/
├── pages/
│   ├── Dashboard.jsx
│   ├── TaskDetail.jsx
│   ├── LogEntry.jsx
│   └── ReportViewer.jsx
├── components/
│   ├── TaskCard.jsx
│   ├── LogForm.jsx
│   └── ReportCard.jsx
├── api/
│   └── guiltometer.js
├── App.jsx
└── main.jsx
```

---

## 🔌 Backend API Endpoints

### 🗂️ Tasks
- `POST /tasks/` → Create new task
- `GET /tasks/` → List all tasks
- `GET /tasks/:id` → Get task detail

### 📝 Logs
- `POST /logs/` → Log daily progress
- `GET /logs/:task_id?start=&end=` → View logs

### 📊 Reports & Roadmaps
- `GET /weekly-report/:task_id` (if exposed)
- `GET /roadmaps/:task_id`

---

## 🧠 Suggested UI Elements

### Dashboard
- List of active tasks
- “+ New Task” button
- Task progress indicators

### Task Detail
- Daily log form with sliders, mood input, notes
- Past logs table

### Weekly Report
- Markdown summary rendering
- Guilt score, suggestions, roadmap if applicable

---

## 📄 Integration Tips

- Add a `.env` with `VITE_API_URL=http://localhost:8000`
- Axios or `fetch()` wrapper in `api/guiltometer.js`
- Use JWT stored in localStorage or use Supabase’s session management
- All requests should pass `Authorization: Bearer <token>` if protected

---

## 🧪 Test API Connection

```js
// api/guiltometer.js
export const getTasks = async () => {
  const res = await fetch(`${import.meta.env.VITE_API_URL}/tasks/`);
  return res.json();
};
```

---

## 🧱 Lightweight UI Libraries (Optional)
- **Headless UI** or **ShadCN UI** (if you want rapid form controls)
- **Heroicons** for icons
- **Markdown Viewer** for weekly reports

---

## ✅ Frontend MVP Features

- [ ] Create and view tasks
- [ ] Log daily metrics
- [ ] View weekly reports (read-only)
- [ ] Simple routing: `/`, `/task/:id`, `/report/:id`

---

## 🧠 Future Add-ons (Optional)
- Calendar view
- Streak visualizer
- Roadmap checklist UI
- Authenticated user dashboard

---

This guide ensures smooth frontend-backend integration, while letting you "vibe code" the UI.
