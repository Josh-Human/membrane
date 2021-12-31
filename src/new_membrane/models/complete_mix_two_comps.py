from new_membrane.components import StreamConstructor
from new_membrane.components import MembraneConstructor
import math


class CompleteMixTwo:
    """Complete mix membrane with two components.

    Transport Processes and Separation Process Principles (Includes Unit Operations) Fourth Edition 13.4
    """

    def __init__(
        self,
        dir: str,
        feed_stream: str,
        reject_stream: str,
        permeate_stream: str,
        membrane: str,
    ) -> None:
        """Given file names and directory for data to construct Streams & Membrane.

        :param _feed_stream: Stream object representing the feed flow.
        :param _reject_stream: Stream object representing the reject flow.
        :param _permeate_stream: Stream object representing the permeate/product flow.
        :param _membrane: Membrane object represnting the membrane.
        :param _sys_vars: Dictionary of the 7 variables neccasary to model a system. xf, xo, yp, θ, alpha, pl/ph, and Am, four of which are independent variables. Full definiton may be found in the class docstring.
        """
        self._feed_stream = StreamConstructor(dir, feed_stream).stream
        self._reject_stream = StreamConstructor(dir, reject_stream).stream
        self._permeate_stream = StreamConstructor(dir, permeate_stream).stream
        self._membrane = MembraneConstructor(dir, membrane).membrane
        self._sys_vars = self._unpack_sys_vars()

    def _unpack_sys_vars(self) -> dict:
        """Unpacks and calculates system variables from Streams & Membrane.

        If values are None then sets to 0.
        """

        xf = list(self._feed_stream.composition.values())[0]

        xo = list(self._reject_stream.composition.values())[0]

        alpha = (
            list(self._membrane.permeability.values())[0]
            / list(self._membrane.permeability.values())[1]
        )

        pr = self._permeate_stream.pressure / self._feed_stream.pressure

        yp = list(self._permeate_stream.composition.values())[0]

        cut = self._permeate_stream.flow / self._reject_stream.flow

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
    def xf(self) -> float:
        """
        :getter: get feed fraction of component A
        """
        return self._sys_vars["xf"]

    @property
    def xo(self) -> float:
        """
        :getter: get reject fraction of component A
        """
        return self._sys_vars["xo"]

    @property
    def alpha(self) -> float:
        """
        :getter: get ratio of permeabilities
        """
        return self._sys_vars["alpha"]

    @property
    def pr(self) -> float:
        """
        :getter: get ratio of pressure
        """
        return self._sys_vars["pr"]

    @property
    def yp(self) -> float:
        """
        :getter: get permeate fraction of component A
        """
        return self._sys_vars["yp"]

    @property
    def area(self) -> float:
        """
        :getter: get total membrane area
        """
        return self._sys_vars["area"]

    @property
    def cut(self) -> float:
        """
        :getter: get ratio of permeate flow to feed flow
        :setter: set cut
        """
        return self._sys_vars["cut"]

    @cut.setter
    def cut(self, value) -> None:
        self._sys_vars["cut"] = value

    def calculate_cut(self) -> float:
        """Find cut value given xf, xo, alpha and pl/ph.

        Calculates yp using root of quadratic equation. This is then used to solve for cut.

        Details of equations used may be found in Class docstring.
        """
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

    def calculate_xo(self) -> float:
        """Find cut value given xf, θ, alpha and pl/ph.

        Calculates yp using root of quadratic equation. This is then used to solve for xo.

        Details of equations used may be found in Class docstring."""
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

    def calculate_area(self) -> float:
        """Calculates total membrane area in cm^2.

        May be called after calculate_xo() or calculate_cut().

        Details of equations used may be found in Class docstring.
        """
        self._sys_vars["area"] = (
            self._sys_vars["cut"] * self._feed_stream.flow * self._sys_vars["yp"]
        ) / (
            (list(self._membrane.permeability.values())[0] / self._membrane.thickness)
            * (
                self._feed_stream.pressure * self._sys_vars["xo"]
                - self._permeate_stream.pressure * self._sys_vars["yp"]
            )
        )
        return self._sys_vars["area"]

    def calculate_min_reject(self) -> float:
        """Given xf, alpha and pl/ph calculates xo.

        Calculates the minimum reject composition based on the feed flow and other system properties. Even with an infintely large membrane the reject can not go below this value for a given composition, however a cascade or plug flow system may be used.

        Details of equations used may be found in Class docstring.
        """
        self._sys_vars["xo"] = (
            self._sys_vars["xf"]
            * (
                1
                + (self._sys_vars["alpha"] - 1)
                * self._sys_vars["pr"]
                * (1 - self._sys_vars["xf"])
            )
        ) / (
            self._sys_vars["alpha"] * (1 - self._sys_vars["xf"]) + self._sys_vars["xf"]
        )
        return self._sys_vars["xo"]


if __name__ == "__main__":
    pass
