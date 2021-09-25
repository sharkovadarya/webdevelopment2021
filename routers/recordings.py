from json import JSONDecodeError
from typing import Optional

from fastapi import APIRouter, HTTPException
from starlette import status
from starlette.responses import Response

from models.models import PostRequest, ShowForTrade, Recordings, Show
from routers.retrieval import find_recordings_by_show_title, find_recordings_by_show_title_and_production
from routers.store import add_show
from util.data import recordings

router = APIRouter()


@router.get("/recordings/")
async def get_recording(title: str, production: Optional[str] = None):
    if production:
        return Recordings(recordings=find_recordings_by_show_title_and_production(title, production))
    return Recordings(recordings=find_recordings_by_show_title(title))


@router.post("/recording-not-for-trade-date/")
async def post_recording_not_for_trade_date(request: PostRequest):
    if request.show_id > len(recordings):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid show ID")
    res = ShowForTrade(show_id=request.show_id, available_in=request.available_in, master=request.master)
    return Response(status_code=status.HTTP_200_OK, headers={"Content-Type": "application/json"},
                    content=res.json())


@router.post("/recording/")
async def post_recording(show: Show):
    try:
        add_show(show)
    except (JSONDecodeError, TypeError, ValueError):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Unable to save recording")
    return show
