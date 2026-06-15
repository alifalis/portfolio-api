from fastapi import FastAPI
from app.routers import projects, skills, contact

app = FastAPI(
    title="Portfolio API",
    description="API REST pour mon portfolio",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Bienvenue sur mon Portfolio API"
    }

app.include_router(contact.router)