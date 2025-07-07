from fastapi import FastAPI
from app.routes import user, cert, course
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="SkillBridge API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router, prefix="/api/user")
app.include_router(cert.router, prefix="/api/cert")
app.include_router(course.router, prefix="/api/courses")
