import time
from enum import Enum
from typing import List

from pydantic import BaseModel, root_validator, validator


class Recording(str, Enum):
    AUDIO = "audio"
    VIDEO = "video"


class Completeness(str, Enum):
    FULL = "full"
    HIGHLIGHTS = "highlights"


class Authorship(str, Enum):
    PROSHOT = "proshot"
    BOOTLEG = "bootleg"


class ShowType(BaseModel):
    recording: Recording
    completeness: Completeness
    authorship: Authorship


class Show(BaseModel):
    title: str
    production: str
    cast: dict
    type: ShowType
    id: int


class Recordings(BaseModel):
    recordings: List[Show] = []


class ShowForTrade(BaseModel):
    show_id: int
    available_in: float  # available in this amount of time counting from the time of the response
    master: str


class PostRequest(BaseModel):
    show_id: int
    available_from: float  # available from this date
    master: str
    available_in: float = None

    @validator('show_id')
    def validate_show_id(cls, v):
        if v < 0:
            raise ValueError('Invalid show ID')
        return v

    # i wanted to make a separate validator but then i couldn't initialize `available_in`
    @root_validator
    def calculate_available_in(cls, values):
        available_in = values['available_from'] - time.time()
        if available_in < 0:
            raise ValueError('NFT date should not be in the past')
        values['available_in'] = available_in
        return values
