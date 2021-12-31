from new_membrane import components
from new_membrane.components import StreamConstructor
from new_membrane.components import MembraneConstructor
import math


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

        pr = self._permeate_stream.pressure / self._input_stream.pressure

        yp = list(self._permeate_stream.composition.values())[0]

        cut = self._permeate_stream.flow / self._output_stream.flow

        area = self._membrane.area
        return {
            "xf": (xf if xf else 0),
            "xo": (xo if xo else 0),
            "alpha": alpha,
            "pr": pr,
            "yp": yp,
            "area": (area if area else 0),
            "cut": cut,
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

    @property
    def cut(self):
        return self._sys_vars["cut"]

    @cut.setter
    def cut(self, value):
        self._sys_vars["cut"] = value

    def calculate_cut(self):
        a = 1 - self._sys_vars["alpha"]

        b = (
            -1
            + self._sys_vars["alpha"]
            + 1 / self._sys_vars["pr"]
            + (self._sys_vars["xo"] / self._sys_vars["pr"])
            * (self._sys_vars["alpha"] - 1)
        )

        c = (-self._sys_vars["alpha"] * self._sys_vars["xo"]) / self._sys_vars["pr"]

        self._sys_vars["yp"] = (-b + math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)

        self._sys_vars["cut"] = (self._sys_vars["xf"] - self._sys_vars["xo"]) / (
            self._sys_vars["yp"] - self._sys_vars["xo"]
        )

        return self._sys_vars["cut"]

    def calculate_area(self):
        self._sys_vars["area"] = (
            self._sys_vars["cut"] * self._input_stream.flow * self._sys_vars["yp"]
        ) / (
            (list(self._membrane.permeability.values())[0] / self._membrane.thickness)
            * (
                self._input_stream.pressure * self._sys_vars["xo"]
                - self._permeate_stream.pressure * self._sys_vars["yp"]
            )
        )
        return self._sys_vars["area"]

    def calculate_xo(self):
        a = (
            self._sys_vars["cut"]
            + self._sys_vars["pr"]
            - self._sys_vars["pr"] * self._sys_vars["cut"]
            - self._sys_vars["alpha"] * self._sys_vars["cut"]
            - self._sys_vars["alpha"] * self._sys_vars["pr"]
            + self._sys_vars["alpha"] * self._sys_vars["pr"] * self._sys_vars["cut"]
        )

        b = (
            1
            - self._sys_vars["cut"]
            - self._sys_vars["xf"]
            - self._sys_vars["pr"]
            + self._sys_vars["pr"] * self._sys_vars["cut"]
            + self._sys_vars["alpha"] * self._sys_vars["cut"]
            + self._sys_vars["alpha"] * self._sys_vars["pr"]
            - self._sys_vars["alpha"] * self._sys_vars["pr"] * self._sys_vars["cut"]
            + self._sys_vars["alpha"] * self._sys_vars["xf"]
        )

        c = -self._sys_vars["alpha"] * self._sys_vars["xf"]

        self._sys_vars["yp"] = (-b + math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)

        self._sys_vars["xo"] = (
            self._sys_vars["xf"] - self._sys_vars["cut"] * self._sys_vars["yp"]
        ) / (1 - self._sys_vars["cut"])

        return self._sys_vars["xo"]


if __name__ == "__main__":
    pass
