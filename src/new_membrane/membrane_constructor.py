import json
import os
from new_membrane.membrane import Membrane


class MembraneConstructor:
    def __init__(self, dir_path: str, file: str) -> None:
        with open(os.path.join(dir_path, file)) as json_file:
            self._data = json.load(json_file)

        self._membrane = self._constructMembrane()

    def _constructMembrane(self) -> None:
        permeability = self._data["permeability"]
        area = self._data["area"]
        dA = self._data["dA"]
        return Membrane(permeability, area, dA)

    @property
    def membrane(self) -> Membrane:

        return self._membrane
