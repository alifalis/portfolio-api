from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import contact, education, projects, profile, skills, experiences

app = FastAPI(
    title="Portfolio API",
    description="API REST pour mon portfolio",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
