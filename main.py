from fastapi import FastAPI
from routers import recordings

app = FastAPI()

app.include_router(recordings.router)