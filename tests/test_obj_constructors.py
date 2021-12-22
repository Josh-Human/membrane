from new_membrane.obj_constructors import StreamConstructor
from new_membrane.stream import Stream
import pytest


class TestStreamConstructor:
    streamConstructor = StreamConstructor("data.json")

    def test_create_instance(self):
        assert isinstance(self.streamConstructor, StreamConstructor)

    def test_stream_constructed(self):
        assert isinstance(self.streamConstructor.stream, Stream)


class TestStreamInputs:
    def test_sum_composition(self):
        with pytest.raises(AssertionError):
            stream = StreamConstructor("invalid_composition_sum.json").stream

    def test_negative_composition(self):
        with pytest.raises(AssertionError):
            stream = StreamConstructor("negative_composition.json").stream

    def test_format_components(self):
        with pytest.raises(AssertionError):
            stream = StreamConstructor("non_dict_composition.json").stream

        with pytest.raises(AssertionError):
            stream = StreamConstructor("non_float_composition.json").stream
