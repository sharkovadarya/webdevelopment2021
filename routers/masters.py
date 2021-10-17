from fastapi import APIRouter

from data.db import find_master_by_recording_id, get_user_info_by_id

router = APIRouter()


@router.get("/master/")
async def get_master_for_recording(recording_id: int):
    return find_master_by_recording_id(recording_id)


@router.get("/user_info/")
async def get_user_info(user_id: int):
    return get_user_info_by_id(user_id)

# @router.post("/recording-not-for-trade-date/")
# async def post_recording_not_for_trade_date(request: PostRequest):
#     if request.show_id > len(recordings):
#         raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid show ID")
#     res = ShowForTrade(show_id=request.show_id, available_in=request.available_in, master=request.master)
#     return Response(status_code=status.HTTP_200_OK, headers={"Content-Type": "application/json"},
#                     content=res.json())
#
#
# @router.post("/recording/")
# async def post_recording(show: Show):
#     try:
#         add_show(show)
#     except (JSONDecodeError, TypeError, ValueError):
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Unable to save recording")
#     return show
