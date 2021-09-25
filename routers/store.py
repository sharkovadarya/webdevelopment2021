import json
import inflection

from models.models import Show
from util.data import recordings, shows, productions

json_path = 'data.json'


def add_show(show: Show):
    show_key = inflection.parameterize(show.title, '_')
    production_key = inflection.parameterize(show.production, '_')
    title = shows.setdefault(show_key, show.title)
    production = productions.setdefault(production_key, show.production)

    if title not in recordings:
        recordings[title] = {}
    if production not in recordings[title]:
        recordings[title][production] = []
    recordings[title][production].append(show)
    write_show_to_json(show, json_path)


def write_show_to_json(show: Show, path_to_json: str):
    with open(path_to_json, "r") as f:
        data = json.load(f)
    data.append(show.dict())
    with open(path_to_json, "w") as f:
        json.dump(data, f, indent=2)
