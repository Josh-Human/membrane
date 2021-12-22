from new_membrane.obj_constructors import StreamConstructor
from new_membrane.stream import Stream
from .conftest import set_up
import pytest


class TestStreamConstructor:
    streamConstructor = StreamConstructor(set_up("data.json"))

    def test_create_instance(self):
        assert isinstance(self.streamConstructor, StreamConstructor)

    def test_stream_constructed(self):
        assert isinstance(self.streamConstructor.stream, Stream)


class TestStreamInputs:
    def test_sum_composition(self):
        with pytest.raises(AssertionError):
            stream = StreamConstructor(
                set_up("data.json", "components", {"CO2": 0.7, "N2": 0.5})
            ).stream

    def test_negative_composition(self):
        with pytest.raises(AssertionError):
            stream = StreamConstructor(
                set_up("data.json", "components", {"CO2": -0.25, "N2": 1.25})
            ).stream

    def test_format_components(self):
        with pytest.raises(AssertionError):
            stream = StreamConstructor(
                set_up("data.json", "components", ["CO2", -0.25, "N2", 1.25])
            ).stream

        with pytest.raises(AssertionError):
            stream = StreamConstructor(
                set_up("data.json", "components", {"CO2": "0.5", "N2": 0.5})
            ).stream
