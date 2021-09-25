import json
from typing import List

from pydantic import parse_obj_as

from models.models import Show

les_miserables = "Les Miserables"
les_miserables_key = "les_miserables"
elisabeth = "Elisabeth"
elisabeth_key = "elisabeth"

shows = {les_miserables_key: les_miserables, elisabeth_key: elisabeth}

les_mis_25_uk_tour_production = "25th Anniversary UK Tour"
les_mis_25_uk_tour_production_key = "25_uk_tour"
les_mis_25_concert_production = "25th Anniversary Concert"
les_mis_25_concert_production_key = "25_concert"
elisabeth_original_vienna_production = "Original Vienna production"
elisabeth_original_vienna_production_key = "original_vienna"

productions = {les_mis_25_uk_tour_production_key: les_mis_25_uk_tour_production,
               les_mis_25_concert_production_key: les_mis_25_concert_production,
               elisabeth_original_vienna_production_key: elisabeth_original_vienna_production}

recordings = {}


def load_recordings_from_json(json_path):
    if len(recordings) > 0:
        return
    with open(json_path) as f:
        data = json.load(f)
    shows_loaded = parse_obj_as(List[Show], data)
    for show in shows_loaded:
        if show.title not in recordings:
            recordings[show.title] = {}
        if show.production not in recordings[show.title]:
            recordings[show.title][show.production] = []
        recordings[show.title][show.production].append(show)


def clear_recordings():
    recordings.clear()
