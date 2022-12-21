from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.config import settings
from app.routers import auth, image, user, project

app = FastAPI()

origins = [
    settings.CLIENT_ORIGIN,
    "http://127.0.0.1:5173",
    "http://127.0.0.1:5173/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth.router, tags=['Auth'], prefix='/api/auth')
app.include_router(user.router, tags=['Users'], prefix='/api/users')
app.include_router(image.router, tags=['Images'], prefix='/api/images')
app.include_router(project.router, tags=['Projects'], prefix='/api/projects')

app.mount("/projects", StaticFiles(directory="projects"), name="projects")

@app.get("/api/healthchecker")
def root():
    return {"message": "Welcome to FastAPI with MongoDB"}
