import json
import os
from new_membrane.membrane import Membrane


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

        self._membrane = self._constructMembrane()

    def _constructMembrane(self) -> None:
        "Unpacks data from file and invokes Membrane object."

        permeability = self._data["permeability"]
        area = self._data["area"]
        dA = self._data["dA"]
        return Membrane(permeability, area, dA)

    @property
    def membrane(self) -> Membrane:
        """
        :getter: get Membrane object
        """
        return self._membrane
