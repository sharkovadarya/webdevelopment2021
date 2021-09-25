import json
import os

import pytest

from routers import store
from routers.retrieval import find_recordings_by_show_title
from routers.store import add_show, write_show_to_json
from util.data import load_recordings_from_json, clear_recordings
from test.test_data.data import elisabeth_vienna_original, les_mis_25_concert, les_mis_25_uk_tour, les_mis_25_uk_tour_audio, \
    tanz_der_vampire_spb
from test.test_util import create_temporary_json_from_file


@pytest.fixture
def json_path():
    dirname = os.path.dirname(__file__)
    path_to_json = os.path.join(dirname, '../../data.json')
    json_path = create_temporary_json_from_file(path_to_json)
    load_recordings_from_json(json_path.name)
    yield json_path.name
    clear_recordings()


class TestStore:
    def test_add_recording(self, json_path):
        store.json_path = json_path
        add_show(tanz_der_vampire_spb)
        res = find_recordings_by_show_title('tanz_der_vampire')
        assert res == [tanz_der_vampire_spb]

    # it's allowed: this service is an index, it does not check file contents (as of now, it does not store the files),
    # and there can be multiple recordings of the same performance
    # plus i haven't even added the performance date yet
    def test_add_duplicate_recording(self, json_path):
        store.json_path = json_path
        add_show(tanz_der_vampire_spb)
        add_show(tanz_der_vampire_spb)
        res = find_recordings_by_show_title('tanz_der_vampire')
        assert res == [tanz_der_vampire_spb, tanz_der_vampire_spb]

    def test_add_slightly_different_title(self, json_path):
        store.json_path = json_path
        add_show(tanz_der_vampire_spb)
        tanz_no_capitals_in_title = tanz_der_vampire_spb
        tanz_no_capitals_in_title.title = "tanz der vampire"
        add_show(tanz_no_capitals_in_title)
        res = find_recordings_by_show_title('tanz_der_vampire')
        # the title will be 'Tanz der Vampire', not 'tanz der vampire'
        # for now the policy is to stick with the first title entered into the system
        assert res == [tanz_der_vampire_spb, tanz_der_vampire_spb]

    def test_write_show_to_json(self, json_path):
        write_show_to_json(tanz_der_vampire_spb, json_path)
        with open(json_path, "r") as f:
            data = json.load(f)
        expected = [les_mis_25_uk_tour, les_mis_25_uk_tour_audio, les_mis_25_concert, elisabeth_vienna_original, tanz_der_vampire_spb]
        assert data == expected

    def test_write_show_to_nonexistent_json(self):
        with pytest.raises(FileNotFoundError):
            write_show_to_json(tanz_der_vampire_spb, 'abracadabra.json')

    def test_write_show_to_malformed_json(self):
        dirname = os.path.dirname(__file__)
        path_to_json = os.path.join(dirname, '../test_data/malformed.json')
        with pytest.raises(json.decoder.JSONDecodeError):
            write_show_to_json(tanz_der_vampire_spb, path_to_json)

    # syntactically correct json but the objects don't form shows
    # it's not this method's responsibility to check whether or not the json file provides correct shows
    def test_write_show_to_incorrect_shows_json(self):
        dirname = os.path.dirname(__file__)
        path_to_json = os.path.join(dirname, '../test_data/incorrect.json')
        path_to_incorrect = create_temporary_json_from_file(path_to_json)
        # no exception should occur
        write_show_to_json(tanz_der_vampire_spb, path_to_incorrect.name)



