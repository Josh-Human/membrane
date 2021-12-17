import json
import os

from new_membrane.stream import Stream
dir_path = os.path.dirname(os.path.realpath(__file__))

class StreamConstructor:
    def __init__(self, file):
        with open(os.path.join(dir_path, file)) as json_file:
            self._data = json.load(json_file)
        
        self.stream = self._constructStream()

    def _constructStream(self):
        return Stream()

    def getStream(self):
        return self.stream


class MembraneConstructor:
    def __init__(self, file):
        with open(os.path.join(dir_path, file)) as json_file:
            self._data = json.load(json_file)
        
        self.membrane = self._constructMembrane()

    def _constructMembrane(self):
        pass

    def getMembrane(self):
        pass