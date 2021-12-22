import json
import os

from new_membrane.stream import Stream

dir_path = os.path.dirname(os.path.realpath(__file__))
used_path = "C:\\Users\\jhuma\\OneDrive\Desktop\python\\new-membrane\\tests\\test_data"
print(used_path)


class StreamConstructor:
    def __init__(self, file):
        with open(os.path.join(used_path, file)) as json_file:
            self._data = json.load(json_file)

        self._check_composition()
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

    def _check_composition(self):
        assert isinstance(self._data["components"], dict), "Non dict value."
        assert all(
            isinstance(self._data["components"][component], float)
            for component in self._data["components"].keys()
        ), "Composition should be float."

        assert (
            sum(self._data["components"].values()) == 1
        ), "Composition does not sum to 1."

        assert all(
            self._data["components"][component] >= 0
            for component in self._data["components"].keys()
        )


# class MembraneConstructor:
#     def __init__(self, file):
#         with open(os.path.join(dir_path, file)) as json_file:
#             self._data = json.load(json_file)

#         self.membrane = self._constructMembrane()

#     def _constructMembrane(self):
#         pass

#     def getMembrane(self):
#         pass
