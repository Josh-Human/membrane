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
            stream = StreamConstructor("invalid_data.json").stream

    def test_negative_composition(self):
        with pytest.raises(AssertionError):
            stream = StreamConstructor("negative_composition.json").stream
