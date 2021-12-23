import pytest
from new_membrane.stream_constructor import StreamConstructor
from new_membrane.membrane_constructor import MembraneConstructor

import json
import os

DIR_PATH = "C:\\Users\\jhuma\\OneDrive\Desktop\python\\new-membrane\\tests\\test_data"


@pytest.fixture(autouse=True)
def stream():
    new_stream = StreamConstructor(set_up("stream_data.json")).stream
    return new_stream


@pytest.fixture(autouse=True)
def stream_constructor():
    new_stream_constructor = StreamConstructor(set_up("stream_data.json"))
    return new_stream_constructor


@pytest.fixture(autouse=True)
def membrane():
    new_membrane = MembraneConstructor(set_up("membrane_data.json")).membrane
    return new_membrane


@pytest.fixture(autouse=True)
def membrane_constructor():
    new_membrane_constructor = MembraneConstructor(set_up("membrane_data.json"))
    return new_membrane_constructor


def set_up(file, key=None, value=None):
    with open(os.path.join(DIR_PATH, file), "w+") as json_file:
        data = {
            "composition": {"CO2": 0.5, "N2": 0.5},
            "flow_rate": 500.0,
            "temperature": 50.0,
            "pressure": 1.0,
        }
        if key:
            data[key] = value

        json.dump(data, json_file)

    return file
