from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from pydantic import BaseModel
from database import engine
from ai_analyzer import analyze_requirement
from typing import Optional
from pydantic import BaseModel, ValidationError



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

class AnalysisResult(BaseModel):
    status: str
    problem: Optional[str] = None
    target_users: Optional[str] = None
    goals: list[str] = []
    requirements: list[str] = []
    open_questions: list[str] = []

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
    if result.get("status") == "error":
        return result   # pass through analyzer-level errors (API failure, bad JSON) as-is

    try:
        validated = AnalysisResult(**result)
        return validated.dict()
    except ValidationError as e:
        return {
            "status": "error",
            "error": "AI response did not match expected schema",
            "details": str(e),
        }