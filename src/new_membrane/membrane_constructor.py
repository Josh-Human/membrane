import json
import os
from new_membrane.membrane import Membrane

DIR_PATH = "C:\\Users\\jhuma\\OneDrive\Desktop\python\\new-membrane\\tests\\test_data"


class MembraneConstructor:
    def __init__(self, file: str):
        with open(os.path.join(DIR_PATH, file)) as json_file:
            self._data = json.load(json_file)

        self.membrane = self._constructMembrane()

    def _constructMembrane(self):
        pass

    def getMembrane(self) -> Membrane:
        pass
