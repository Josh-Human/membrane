from new_membrane.components import StreamConstructor
from new_membrane.components import MembraneConstructor
import scipy.optimize


class CompleteMix:
    """Complete mixing model membrane with multiple components.

    Transport Processes and Separation Process Principles (Includes Unit Operations) Fourth Edition 13.5
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

        """
        self._feed_stream = StreamConstructor(dir, feed_stream).stream
        self._reject_stream = StreamConstructor(dir, reject_stream).stream
        self._permeate_stream = StreamConstructor(dir, permeate_stream).stream
        self._membrane = MembraneConstructor(dir, membrane).membrane

        # Known values
        self._feed_composition = list(self._feed_stream.composition.values())
        self._feed_flow = self._feed_stream.flow

        self._pl = self._permeate_stream.pressure
        self._ph = self._feed_stream.pressure

        self._permeabilities = list(self._membrane.permeability.values())
        self._thickness = self._membrane.thickness

        self._cut = (
            self._permeate_stream.flow / self._reject_stream.flow
            if self._permeate_stream.flow / self._reject_stream.flow
            else 0
        )

        # Unkown values
        self._ypa = None
        self._vp = None

        self._unknown_vars = {}

    @property
    def feed_composition(self) -> None:
        """
        :getter: get feed stream composition
        """
        return self._feed_stream.composition

    @property
    def feed_flow(self) -> float:
        """
        :getter: get feed stream total flowrate
        """
        return self._feed_stream.flow

    @property
    def cut(self) -> float:
        """
        :getter: get cut of system
        :setter: set cut of system
        """
        return self._cut

    @cut.setter
    def cut(self, value: float) -> None:
        self._cut = value

    @property
    def pl(self) -> float:
        """
        :getter: get retenate pressure
        """
        return self._feed_stream.pressure

    @property
    def ph(self) -> float:
        """
        :getter: get feed side pressure
        """
        return self._permeate_stream.pressure

    @property
    def permeabilities(self) -> dict:
        """
        :getter: get permeability of components
        """
        return self._membrane.permeability

    @property
    def thickness(self) -> float:
        """
        :getter: get membrane thickness in m
        """
        return self._membrane.thickness

    @property
    def permeate_composition(self) -> dict:
        """
        :getter: get permeate composition
        """
        return self._permeate_stream.composition

    def calculate_permeate_composition(self, initial_guess: float = None) -> float:
        """Calculates permeate composition and returns a value for root finding.

        Permeate composition of component A is used as an initial value for root finding, being either calculated or set. Return a value to be used in the newton method to find the final permeate composition.
        """
        self._set_permeate_composition(initial_guess)
        self._calculate_permeate_flow()
        self._calculate_area()
        self._calculate_permeate_compositions()
        # Calculate compositions overwrites initial set which is unwanted, so repeated.
        self._set_permeate_composition(initial_guess)
        return 1 - sum(self._permeate_stream.composition.values())

    def _set_permeate_composition(self, initial_guess: float = None) -> None:
        """Sets mole fraction of component A."""
        if initial_guess:
            self._permeate_stream.composition = [initial_guess]
            self._ypa = initial_guess
        else:
            self._permeate_stream.composition = [self._feed_composition[0] + 0.01]
            self._ypa = self._feed_composition[0] + 0.01

    def _calculate_permeate_flow(self) -> None:
        """Permeate flow is calculated using current composition guess."""
        self._permeate_stream.flow = self._cut * self._feed_flow
        self._vp = self._cut * self._feed_flow

    def _calculate_area(self) -> None:
        """Membrane area calculated using current iteration values."""
        self._membrane.area = (
            self._permeate_stream.flow * self._ypa * self._membrane.thickness
        ) / (
            self._permeabilities[0]
            * (
                (self._ph / (1 - self._cut))
                * (self._feed_composition[0] - self._cut * self._ypa)
                - self._pl * self._ypa
            )
        )

    def _calculate_permeate_compositions(self) -> None:
        """All permeate compositions calculated.

        Although all permeate compositions are calculated, component A should not be. As a result after this function is called component A is reset  to the iteration guess value after.
        """
        for k in self._permeate_stream.composition.keys():
            self._permeate_stream.composition[k] = (
                self._ph * self._feed_stream.composition[k] / (1 - self._cut)
            ) / (
                (
                    self._vp
                    * self._thickness
                    / (self._membrane.permeability[k] * self._membrane.area)
                )
                + (self._cut * self._ph) / (1 - self._cut)
                + self._pl
            )

    def calculate_reject_composition(self, yp0: float = None) -> dict:
        """Calculate and return reject composition.

        Finds final permeate composition, which is then used to calculate other system values and finally the reject composition.
        """
        scipy.optimize.newton(self.calculate_permeate_composition, yp0)

        for k in self._reject_stream.composition.keys():
            self._reject_stream.composition[k] = self._feed_stream.composition[k] / (
                1 - self._cut
            ) - (self._cut * self._permeate_stream.composition[k]) / (1 - self._cut)

        return self._reject_stream.composition
