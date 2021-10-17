import json
import os
import tempfile
import unittest

import pytest
from fastapi.testclient import TestClient

import main
from main import app
from routers import store


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


class TestDB:
    def test_get_master_for_recording(self, json_path):
        main.json_path = json_path
        store.json_path = json_path
        with TestClient(app) as client:
            response = client.get("/master/?recording_id=0")
            assert response.status_code == 200
            assert response.json() == 1

    def test_get_user_info(self, json_path):
        main.json_path = json_path
        store.json_path = json_path
        with TestClient(app) as client:
            response = client.get("/user_info/?user_id=1")
            assert response.status_code == 200
            assert response.json() == {'user': 'barricadegirl', 'email': 'barricadegirl@abaisse.net'}


if __name__ == '__main__':
    unittest.main()
