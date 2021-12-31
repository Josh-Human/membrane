import pytest
from new_membrane.components import StreamConstructor
from new_membrane.components import MembraneConstructor

import json
import os

DIR_PATH = "C:\\Users\\jhuma\\OneDrive\Desktop\python\\new-membrane\\tests\\test_data"


@pytest.fixture()
def stream():
    new_stream = StreamConstructor(DIR_PATH, set_up("stream_data.json")).stream
    return new_stream


@pytest.fixture()
def stream_constructor():
    new_stream_constructor = StreamConstructor(DIR_PATH, set_up("stream_data.json"))
    return new_stream_constructor


@pytest.fixture()
def membrane():
    new_membrane = MembraneConstructor(
        DIR_PATH, set_up_membrane("membrane_data.json")
    ).membrane
    return new_membrane


@pytest.fixture()
def membrane_constructor():
    new_membrane_constructor = MembraneConstructor(
        DIR_PATH, set_up_membrane("membrane_data.json")
    )
    return new_membrane_constructor


def set_up_membrane(file, key=None, value=None):
    with open(os.path.join(DIR_PATH, file), "w+") as json_file:
        data = {"permeability": {"CO2": 5, "N2": 5}, "area": 500, "dA": 10}
        if key == "data":
            data = value
        elif key:
            data[key] = value

        json.dump(data, json_file)

    return file


def set_up(file, key=None, value=None):
    with open(os.path.join(DIR_PATH, file), "w+") as json_file:
        data = {
            "composition": {"CO2": 0.5, "N2": 0.5},
            "flow_rate": 500.0,
            "temperature": 50.0,
            "pressure": 1.0,
        }
        if key == "data":
            data = value
        elif key:
            data[key] = value

        json.dump(data, json_file)

    return file


if __name__ == "__main__":
    pass
