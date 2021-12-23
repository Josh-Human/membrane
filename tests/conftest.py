import json
import os

dir_path = "C:\\Users\\jhuma\\OneDrive\Desktop\python\\new-membrane\\tests\\test_data"


def set_up(file, key=None, value=None):
    with open(os.path.join(dir_path, file), "w+") as json_file:
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
