from fastapi import APIRouter, HTTPException
from starlette import status
from starlette.responses import Response

from models.models import PostRequest, ShowForTrade, Recordings
from util.data import recordings

router = APIRouter()


@router.get("/recordings/")
async def get_recording(title):
    if title == "les_miserables":
        return Recordings(recordings=[recordings[0], recordings[1]])
    elif title == "elisabeth":
        return Recordings(recordings=[recordings[2]])
    return Recordings()


@router.post("/recording-not-for-trade-date/")
async def post_recording_not_for_trade_date(request: PostRequest):
    if request.show_id > len(recordings):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid show ID")
    res = ShowForTrade(show_id=request.show_id, available_in=request.available_in, master=request.master)
    return Response(status_code=status.HTTP_200_OK, headers={"Content-Type": "application/json"},
                    content=res.json())