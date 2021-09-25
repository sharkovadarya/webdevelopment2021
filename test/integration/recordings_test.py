import json
import os
import tempfile
import unittest
from typing import List

import pytest
from fastapi.testclient import TestClient
from pydantic import parse_obj_as

import main
from main import app
from models.models import Show
from routers import store
from test.test_data.data import les_mis_25_uk_tour, les_mis_25_uk_tour_audio, les_mis_25_concert, elisabeth_vienna_original, \
    tanz_der_vampire_spb


@pytest.fixture
def json_path():
    dirname = os.path.dirname(__file__)
    path_to_json = os.path.join(dirname, '../../data.json')
    with open(path_to_json) as f:
        data = json.load(f)
    json_path = tempfile.NamedTemporaryFile('r+')
    json.dump(data, json_path, indent=2)
    json_path.flush()
    yield json_path.name


class TestRecordings:
    def test_get_by_title(self, json_path):
        main.json_path = json_path
        store.json_path = json_path
        with TestClient(app) as client:
            response = client.get("/recordings/?title=elisabeth")
            assert response.status_code == 200
            shows = parse_obj_as(List[Show], response.json()['recordings'])
            assert shows == [elisabeth_vienna_original]

    def test_get_by_title_multiple_productions(self, json_path):
        main.json_path = json_path
        store.json_path = json_path
        with TestClient(app) as client:
            response = client.get("/recordings/?title=les_miserables")
            assert response.status_code == 200
            shows = parse_obj_as(List[Show], response.json()['recordings'])
            assert shows == [les_mis_25_uk_tour, les_mis_25_uk_tour_audio, les_mis_25_concert]

    def test_get_by_title_not_found(self, json_path):
        main.json_path = json_path
        store.json_path = json_path
        with TestClient(app) as client:
            response = client.get("/recordings/?title=next_to_normal")
            assert response.status_code == 200
            shows = parse_obj_as(List[Show], response.json()['recordings'])
            assert len(shows) == 0

    def test_post_recording(self, json_path):
        main.json_path = json_path
        store.json_path = json_path
        with TestClient(app) as client:
            response = client.post("/recording/", json=tanz_der_vampire_spb.dict())
            assert response.status_code == 200
            assert response.json() == tanz_der_vampire_spb.dict()

    def test_post_and_get_recording(self, json_path):
        main.json_path = json_path
        store.json_path = json_path
        with TestClient(app) as client:
            response = client.post("/recording/", json=tanz_der_vampire_spb.dict())
            assert response.status_code == 200
            assert response.json() == tanz_der_vampire_spb.dict()
            response = client.get("/recordings/?title=tanz_der_vampire")
            assert response.status_code == 200
            shows = parse_obj_as(List[Show], response.json()['recordings'])
            assert shows == [tanz_der_vampire_spb]

    def test_post_malformed_recording(self, json_path):
        main.json_path = json_path
        store.json_path = json_path
        with TestClient(app) as client:
            malformed_recording = tanz_der_vampire_spb.dict()
            malformed_recording['type'] = 'something'
            response = client.post("/recording/", json=malformed_recording)
            assert response.status_code == 422


if __name__ == '__main__':
    unittest.main()
