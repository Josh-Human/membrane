from new_membrane import components
from new_membrane.components import StreamConstructor
from new_membrane.components import MembraneConstructor


class CompleteMixTwo:
    """
    Transport Processes and Separation Process Principles (Includes Unit Operations) Fourth Edition 13.4
    """

    def __init__(
        self, dir, input_stream, output_stream, permeate_stream, membrane
    ) -> None:
        self._input_stream = StreamConstructor(dir, input_stream).stream
        self._output_stream = StreamConstructor(dir, output_stream).stream
        self._permeate_stream = StreamConstructor(dir, permeate_stream).stream
        self._membrane = MembraneConstructor(dir, membrane).membrane
        self._sys_vars = self._unpack_sys_vars()

    def _unpack_sys_vars(self):

        xf = list(self._input_stream.composition.values())[0]

        xo = list(self._output_stream.composition.values())[0]

        alpha = (
            list(self._membrane.permeability.values())[0]
            / list(self._membrane.permeability.values())[1]
        )

        pr = self._input_stream.pressure / self._permeate_stream.pressure

        yp = list(self._permeate_stream.composition.values())[0]

        area = self._membrane.area
        return {
            "xf": (xf if xf else 0),
            "xo": (xo if xo else 0),
            "alpha": alpha,
            "pr": pr,
            "yp": yp,
            "area": (area if area else 0),
        }

    @property
    def xf(self):
        return self._sys_vars["xf"]

    @property
    def xo(self):
        return self._sys_vars["xo"]

    @property
    def alpha(self):
        return self._sys_vars["alpha"]

    @property
    def pr(self):
        return self._sys_vars["pr"]

    @property
    def yp(self):
        return self._sys_vars["yp"]

    @property
    def area(self):
        return self._sys_vars["area"]


if __name__ == "__main__":
    pass
