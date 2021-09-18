import json
from enum import Enum


class Recording(str, Enum):
    AUDIO = "audio"
    VIDEO = "video"


class Completeness(str, Enum):
    FULL = "full"
    HIGHLIGHTS = "highlights"


class Authorship(str, Enum):
    PROSHOT = "proshot"
    BOOTLEG = "bootleg"


class ShowType(object):
    def __init__(self, recording, completeness, authorship):
        self.recording_type = recording
        self.completeness = completeness
        self.authorship = authorship

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class Show:
    def __init__(self, title, production, cast, type, id):
        self.title = title
        self.production = production
        self.cast = cast
        self.type = type
        self.id = id

    def to_json(self):
        json.dumps(self, default=lambda o: o.__dict__)
