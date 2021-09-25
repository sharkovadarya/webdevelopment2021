import json
import tempfile


def create_temporary_json_from_file(json_path):
    with open(json_path) as f:
        data = json.load(f)
    temp_json = tempfile.NamedTemporaryFile('r+')
    json.dump(data, temp_json, indent=2)
    temp_json.flush()
    return temp_json
