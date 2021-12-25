import json
import os
from typing import Type
from new_membrane.stream import Stream
from .utils.utils import check_dict_values_postive

DIR_PATH = "C:\\Users\\jhuma\\OneDrive\Desktop\python\\new-membrane\\tests\\test_data"


class StreamConstructor:
    def __init__(self, file: str):
        with open(os.path.join(DIR_PATH, file)) as json_file:
            self._data = json.load(json_file)
        self._convert_ints()
        self._check_inputs()
        self._stream = self._constructStream()

    def _constructStream(self):
        composition = self._data["composition"]
        flow = self._data["flow_rate"]
        temp = self._data["temperature"]
        pressure = self._data["pressure"]
        return Stream(composition, flow, temp, pressure)

    @property
    def stream(self) -> Stream:
        return self._stream

    def _check_type(self):

        if not isinstance(self._data["composition"], dict):
            raise TypeError("Composition should be type dict.")

        compositions_are_float = all(
            isinstance(self._data["composition"][component], float)
            for component in self._data["composition"].keys()
        )

        if not compositions_are_float:
            raise TypeError("composition values should be floats.")

        if not isinstance(self._data["pressure"], float):
            raise TypeError("Pressure should be type float.")

        if not isinstance(self._data["temperature"], float):
            raise TypeError("Temperature should be type float.")

        if not isinstance(self._data["flow_rate"], float):
            raise TypeError("Flow rate should be type float.")

    def _check_value(self):
        if sum(self._data["composition"].values()) != 1:
            raise ValueError("Composition does not sum to 1.")

        if check_dict_values_postive(self._data["composition"]):
            raise ValueError("Composition values should all be positive.")

        if self._data["pressure"] < 0:
            raise ValueError("Presure below 0.")

        if self._data["flow_rate"] < 0:
            raise ValueError("Flow rate below 0.")

    def _check_inputs(self):

        self._check_type()
        self._check_value()

    def _convert_ints(self):
        if isinstance(self._data["composition"], dict):
            composition_are_int = all(
                isinstance(self._data["composition"][component], int)
                for component in self._data["composition"].keys()
            )
            if composition_are_int:
                for k, v in self._data["composition"]:
                    self._data["composition"][k] = float(v)

        if isinstance(self._data["pressure"], int):
            self._data["pressure"] = float(self._data["pressure"])

        if isinstance(self._data["temperature"], int):
            self._data["temperature"] = float(self._data["temperature"])

        if isinstance(self._data["flow_rate"], int):
            self._data["flow_rate"] = float(self._data["flow_rate"])
