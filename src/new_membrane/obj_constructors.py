import json
import os
from typing import Type

from new_membrane.stream import Stream

dir_path = os.path.dirname(os.path.realpath(__file__))
used_path = "C:\\Users\\jhuma\\OneDrive\Desktop\python\\new-membrane\\tests\\test_data"
print(used_path)


class StreamConstructor:
    def __init__(self, file):
        with open(os.path.join(used_path, file)) as json_file:
            self._data = json.load(json_file)
        self._convert_ints()
        self._check_inputs()
        self._stream = self._constructStream()

    def _constructStream(self):
        components = self._data["components"]
        flow = self._data["flow_rate"]
        temp = self._data["temperature"]
        pressure = self._data["pressure"]
        return Stream(components, flow, temp, pressure)

    @property
    def stream(self):
        return self._stream

    def _check_type(self):

        if not isinstance(self._data["components"], dict):
            raise TypeError("Components should be type dict.")

        components_are_float = all(
            isinstance(self._data["components"][component], float)
            for component in self._data["components"].keys()
        )

        if not components_are_float:
            raise TypeError("Components values should be floats.")

        if not isinstance(self._data["pressure"], float):
            raise TypeError("Pressure should be type float.")

        if not isinstance(self._data["temperature"], float):
            raise TypeError("Temperature should be type float.")

        if not isinstance(self._data["flow_rate"], float):
            raise TypeError("Flow rate should be type float.")

    def _check_value(self):
        if sum(self._data["components"].values()) != 1:
            raise ValueError("Composition does not sum to 1.")

        composition_all_positive = all(
            self._data["components"][component] >= 0
            for component in self._data["components"].keys()
        )

        if not composition_all_positive:
            raise ValueError("Composition values should all be positive.")

        if self._data["pressure"] < 0:
            raise ValueError("Presure below 0.")

        if self._data["flow_rate"] < 0:
            raise ValueError("Flow rate below 0.")

    def _check_inputs(self):

        self._check_type()
        self._check_value()

    def _convert_ints(self):
        if isinstance(self._data["components"], dict):
            components_are_int = all(
                isinstance(self._data["components"][component], int)
                for component in self._data["components"].keys()
            )
            if components_are_int:
                for k, v in self._data["components"]:
                    self._data["components"][k] = float(v)

        if isinstance(self._data["pressure"], int):
            self._data["pressure"] = float(self._data["pressure"])

        if isinstance(self._data["temperature"], int):
            self._data["temperature"] = float(self._data["temperature"])

        if isinstance(self._data["flow_rate"], int):
            self._data["flow_rate"] = float(self._data["flow_rate"])


# class MembraneConstructor:
#     def __init__(self, file):
#         with open(os.path.join(dir_path, file)) as json_file:
#             self._data = json.load(json_file)

#         self.membrane = self._constructMembrane()

#     def _constructMembrane(self):
#         pass

#     def getMembrane(self):
#         pass
