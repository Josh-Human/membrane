import json
import os
from new_membrane.components.membrane import Membrane
from numbers import Number as num
from new_membrane.utils.utils import check_all_values_number, check_values_positive


class MembraneConstructor:
    """Creates Membrane object from data file.

    Checks data file for valid data types and values, constructing a Membrane object to be returned.
    """

    def __init__(self, dir_path: str, file: str) -> None:
        """Initalizes MembraneConstructor from data file.

        :param _membrane: Membrane object to be returned
        """
        with open(os.path.join(dir_path, file)) as json_file:
            self._data = json.load(json_file)
        self._check_input()
        self._membrane = self._constructMembrane()

    def _constructMembrane(self) -> None:
        "Unpacks data from file and invokes Membrane object."

        permeability = self._data["permeability"]
        area = self._data["area"]
        dA = self._data["dA"]
        thickness = self._data["thickness"]
        return Membrane(permeability, area, dA, thickness)

    @property
    def membrane(self) -> Membrane:
        """
        :getter: get Membrane object
        """
        return self._membrane

    def _check_value(self) -> None:
        """Checks data file for valid values.

        Checks Permeability sums to 1 and has no negative values.
        Checks pressure and flowrate are positive.

        raises ValueError
        """

        if not check_values_positive(self._data["permeability"]):
            raise ValueError("Permeability values should all be positive.")

        if self._data["area"] < 0:
            raise ValueError("Area should be positive.")

        if self._data["dA"] < 0:
            raise ValueError("dA should be positive.")

    def _check_input(self):
        # self._check_type()
        self._check_value()

        if self._data["area"] < self._data["dA"]:
            raise ValueError("dA should be smaller than area.")


if __name__ == "__main__":
    pass

# def _check_type(self) -> None:
#     """Checks data file for valid types.

#     Checks permeability is a dict with str:Number entries.
#     Checks area and dA are Numbers.

#     raises TypeError
#     """
#     if not isinstance(self._data["permeability"], dict):
#         raise TypeError("Permeability should be type dict.")

#     if not check_all_values_number(self._data["permeability"]):
#         raise TypeError("Permeability values should be Numbers.")

#     if not isinstance(self._data["area"], num):
#         raise TypeError("Area should be type Number.")

# if not isinstance(self._data["dA"], num):
#     raise TypeError("dA should be type Number.")
