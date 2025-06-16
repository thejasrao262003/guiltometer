from fastapi import FastAPI
from app.routers.users import router as user_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health-check")
def health_check():
    return {"message": "Backend is running"}

app.include_router(user_router, prefix="/api/users")