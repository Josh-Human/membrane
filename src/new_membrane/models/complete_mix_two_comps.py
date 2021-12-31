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

        composition_in = list(self._input_stream.composition.values())

        composition_out = list(self._output_stream.composition.values())

        alpha = (
            list(self._membrane.permeability.values())[0]
            / list(self._membrane.permeability.values())[1]
        )

        return {
            "xf": (composition_in[0] if composition_in[0] else 0),
            "xo": (composition_out[0] if composition_out[0] else 0),
            "alpha": alpha,
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


if __name__ == "__main__":
    pass
