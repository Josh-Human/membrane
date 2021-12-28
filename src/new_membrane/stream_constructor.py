import json
import os
from numbers import Number as num
from typing import Type
from new_membrane.stream import Stream
from .utils.utils import check_all_values_number, check_values_positive


class StreamConstructor:
    """Creates Stream object from data file.

    Checks data file for valid data types and values, constructing a Stream object to be returned.
    """

    def __init__(self, dir_path: str, file: str) -> None:
        """Initalizes StreamConstructor from data file.

        :param _stream: Stream object to be returned
        """
        with open(os.path.join(dir_path, file)) as json_file:
            self._data = json.load(json_file)
        self._check_inputs()
        self._stream = self._constructStream()

    def _constructStream(self) -> Stream:
        "Unpacks data from file and invokes Stream object."

        composition = self._data["composition"]
        flow = self._data["flow_rate"]
        temp = self._data["temperature"]
        pressure = self._data["pressure"]
        return Stream(composition, flow, temp, pressure)

    @property
    def stream(self) -> Stream:
        """
        :getter: get Stream object
        """
        return self._stream

    def _check_type(self) -> None:
        """Checks data file for valid types.

        Checks compoisiton is a dict with str:float entries.
        Checks pressure, temperature and flow_rate are floats.

        raises TypeError
        """
        if not isinstance(self._data["composition"], dict):
            raise TypeError("Composition should be type dict.")

        if not check_all_values_number(self._data["composition"]):
            raise TypeError("Composition values should be Numbers.")

        if not isinstance(self._data["pressure"], num):
            raise TypeError("Pressure should be type Number.")

        if not isinstance(self._data["temperature"], num):
            raise TypeError("Temperature should be type Number.")

        if not isinstance(self._data["flow_rate"], num):
            raise TypeError("Flow rate should be type Number.")

    def _check_value(self) -> None:
        """Checks data file for valid values.

        Checks composition sums to 1 and has no negative values.
        Checks pressure and flowrate are positive.

        raises ValueError
        """
        if sum(self._data["composition"].values()) != 1:
            raise ValueError("Composition does not sum to 1.")

        if not check_values_positive(self._data["composition"]):
            raise ValueError("Composition values should all be positive.")

        if self._data["pressure"] < 0:
            raise ValueError("Pressure below 0.")

        if self._data["flow_rate"] < 0:
            raise ValueError("Flow rate below 0.")

    def _check_inputs(self) -> None:
        """Check data file types and values."""
        self._check_type()
        self._check_value()

    def _convert_ints(self) -> None:
        """Converts int values to float."""
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
