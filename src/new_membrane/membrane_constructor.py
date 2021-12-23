import json
import os
from new_membrane.membrane import Membrane

DIR_PATH = "C:\\Users\\jhuma\\OneDrive\Desktop\python\\new-membrane\\tests\\test_data"


class MembraneConstructor:
    def __init__(self, file: str):
        with open(os.path.join(DIR_PATH, file)) as json_file:
            self._data = json.load(json_file)

        self._membrane = self._constructMembrane()

    def _constructMembrane(self):
        permeability = self._data["permeability"]
        area = self._data["area"]
        dA = self._data["dA"]
        return Membrane(permeability, area, dA)

    @property
    def membrane(self) -> Membrane:

        return self._membrane
