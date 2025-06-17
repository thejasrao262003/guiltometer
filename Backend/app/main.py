from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.users import router as user_router
from app.routers.tasks import router as task_router
from app.routers.daily_logs import router as daily_logs_router
from app.routers.roadmaps import router as roadmaps_router
from app.routers.weekly_reports import router as weekly_reports_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can tighten this for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health-check")
def health_check():
    return {"message": "Backend is running"}

# ✅ Consistent API versioning and route naming
app.include_router(user_router, prefix="/api/users")
app.include_router(task_router, prefix="/api/tasks")
app.include_router(daily_logs_router, prefix="/api/daily-logs")
app.include_router(weekly_reports_router, prefix="/api/weekly-reports")
app.include_router(roadmaps_router, prefix="/api/roadmaps")
