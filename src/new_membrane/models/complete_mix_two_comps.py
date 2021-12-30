from new_membrane.components import StreamConstructor
from new_membrane.components import MembraneConstructor


class CompleteMixTwo:
    def __init__(self, dir, input_stream, output_stream, membrane) -> None:
        self._input_stream = StreamConstructor(dir, input_stream)
        self._output_stream = StreamConstructor(dir, output_stream)
        self._membrane = MembraneConstructor(dir, membrane)


if __name__ == "__main__":
    pass
