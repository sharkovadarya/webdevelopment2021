import time

from fastapi import FastAPI, HTTPException
from starlette import status
from starlette.responses import Response

from models import PostRequest, ShowForTrade
from show import Show, ShowType, Recording, Completeness, Authorship

app = FastAPI()

recordings = [
    Show("Les Miserables", "25th Anniversary UK Tour", {
        "Jean Valjean": "John Owen-Jones",
        "Javert": "Earl Carpenter",
        "Fantine": "Madalena Alberto"
    }, ShowType(Recording.VIDEO, Completeness.FULL, Authorship.BOOTLEG), 0),
    Show("Les Miserables", "25th Anniversary Concert", {
        "Jean Valjean": "Alfie Boe",
        "Javert": "Norm Lewis",
        "Fantine": "Lea Salonga"
    }, ShowType(Recording.VIDEO, Completeness.FULL, Authorship.PROSHOT), 1),
    Show("Elisabeth", "Original Vienna production", {
        "Elisabeth": "Pia Douwes",
        "Death": "Uwe Kroger"
    }, ShowType(Recording.AUDIO, Completeness.HIGHLIGHTS, Authorship.PROSHOT), 2)
]


@app.get("/recordings/")
async def get_recording(title):
    if title == "les_miserables":
        return {"recordings": [recordings[0], recordings[1]]}
    elif title == "elisabeth":
        return {"recordings": [recordings[2]]}
    return {"recordings": []}


@app.post("/recording-not-for-trade-date/")
async def post_recording_not_for_trade_date(request: PostRequest):
    available_in = request.available_from - time.time()
    if available_in < 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="NFT date is already in the past")
    if request.show_id < 0 or request.show_id >= len(recordings):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid show ID")

    res = ShowForTrade(show_id=request.show_id, available_in=available_in, master=request.master)
    return Response(status_code=status.HTTP_200_OK, headers={"Content-Type": "application/json"},
                    content=res.json())
