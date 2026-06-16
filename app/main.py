from fastapi import FastAPI

from app.routers import contact, education, projects, profile, skills, experiences

app = FastAPI(
    title="Portfolio API",
    description="API REST pour mon portfolio",
    version="1.0.0"
)


@app.get("/", tags=["Home"])
def home():
    return {
        "message": "Bienvenue sur mon Portfolio API",
        "documentation": "/docs"
    }


app.include_router(contact.router)
app.include_router(education.router)
app.include_router(projects.router)
