import os

import pytest

from routers.retrieval import find_recordings_by_show_title
from util.data import load_recordings_from_json, clear_recordings
from test.test_data.data import elisabeth_vienna_original, les_mis_25_concert, les_mis_25_uk_tour, les_mis_25_uk_tour_audio
from test.test_util import create_temporary_json_from_file


@pytest.fixture
def json_path():
    dirname = os.path.dirname(__file__)
    path_to_json = os.path.join(dirname, '../../data.json')
    json_path = create_temporary_json_from_file(path_to_json)
    load_recordings_from_json(json_path.name)
    yield json_path.name
    clear_recordings()


@pytest.mark.usefixtures('json_path')
class TestRetrieval:
    def test_find_recordings_by_show_title(self):
        res = find_recordings_by_show_title('elisabeth')
        assert res == [elisabeth_vienna_original]

    def test_find_recordings_by_show_title_multiple_productions(self):
        res = find_recordings_by_show_title('les_miserables')
        assert res == [les_mis_25_uk_tour, les_mis_25_uk_tour_audio, les_mis_25_concert]

    def test_find_recordings_by_show_title_not_found(self):
        res = find_recordings_by_show_title('tanz_der_vampire')
        assert res == []


