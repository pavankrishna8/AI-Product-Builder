from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from pydantic import BaseModel
from database import engine
from ai_analyzer import analyze_requirement

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class RequirementCreate(BaseModel):
    title: str
    description: str

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/db-check")
def db_check():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    return {"database": "connected"}

@app.post("/requirements")
def create_requirement(requirement: RequirementCreate):
    return {
        "message": "Requirement received",
        "data": requirement.dict()
    }

@app.post("/requirements/analyze")
def analyze(requirement: RequirementCreate):
    result = analyze_requirement(requirement.description)
    return result