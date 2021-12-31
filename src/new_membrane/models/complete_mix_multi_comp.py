from new_membrane.components import StreamConstructor
from new_membrane.components import MembraneConstructor
import math


class CompleteMix:
    """Complete mix membrane with multiple components.

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
        self._known_vars = self._unpack_known_vars()

    @property
    def feed_composition(self):
        return self._feed_stream.composition

    def _unpack_known_vars(self) -> dict:
        """Unpacks and calculates system variables from Streams & Membrane.

        If values are None then sets to 0.
        """
        pass
