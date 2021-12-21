import json
import os

from new_membrane.stream import Stream
dir_path = os.path.dirname(os.path.realpath(__file__))

class StreamConstructor:
    def __init__(self, file):
        with open(os.path.join(dir_path, file)) as json_file:
            self._data = json.load(json_file)
        
        self._stream = self._constructStream()

    def _constructStream(self):
        components = self._data['components']
        flow = self._data['flow_rate']
        temp = self._data['temperature']
        pressure = self._data['pressure']
        return Stream(components, flow, temp, pressure)

    @property
    def stream(self):
        return self._stream









# class MembraneConstructor:
#     def __init__(self, file):
#         with open(os.path.join(dir_path, file)) as json_file:
#             self._data = json.load(json_file)
        
#         self.membrane = self._constructMembrane()

#     def _constructMembrane(self):
#         pass

#     def getMembrane(self):
#         pass