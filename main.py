from fastapi import FastAPI

from routers import recordings
from util.data import load_recordings_from_json, clear_recordings

app = FastAPI()

app.include_router(recordings.router)

json_path = 'data.json'


@app.on_event("startup")
def startup_event():
    load_recordings_from_json(json_path)


@app.on_event("shutdown")
def shutdown_event():
    clear_recordings()
