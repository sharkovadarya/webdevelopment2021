from pydantic import BaseModel

from show import Recording, Completeness, Authorship


class ShowTypeModel(BaseModel):
    recording: Recording
    completeness: Completeness
    authorship: Authorship


class ShowModel(BaseModel):
    title: str
    production: str
    cast: dict
    type: ShowTypeModel
    id: int


class ShowForTrade(BaseModel):
    show_id: int
    available_in: float  # available in this amount of time counting from the time of the response
    master: str


class PostRequest(BaseModel):
    show_id: int
    available_from: float  # available from this date
    master: str
