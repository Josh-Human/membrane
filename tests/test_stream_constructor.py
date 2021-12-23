from new_membrane.stream_constructor import StreamConstructor
from new_membrane.stream import Stream
import pytest
from .conftest import set_up


class TestStreamConstructor:
    def test_create_instance(self, stream_constructor):
        assert isinstance(stream_constructor, StreamConstructor)

    def test_stream_constructed(self, stream):
        assert isinstance(stream, Stream)


class TestStreamInputs:
    def test_sum_composition(self):
        with pytest.raises(ValueError):
            stream = StreamConstructor(
                set_up("data.json", "composition", {"CO2": 0.7, "N2": 0.5})
            ).stream

    def test_negative_composition(self):
        with pytest.raises(ValueError):
            stream = StreamConstructor(
                set_up("data.json", "composition", {"CO2": -0.25, "N2": 1.25})
            ).stream

    def test_format_composition(self):
        with pytest.raises(TypeError):
            stream = StreamConstructor(
                set_up("data.json", "composition", ["CO2", 0.5, "N2", 0.5])
            ).stream

        with pytest.raises(TypeError):
            stream = StreamConstructor(
                set_up("data.json", "composition", {"CO2": "0.5", "N2": 0.5})
            ).stream

    def test_pressure_positive(self):
        with pytest.raises(ValueError):
            stream = StreamConstructor(set_up("data.json", "pressure", -0.1)).stream

    def test_flow_positive(self):
        with pytest.raises(ValueError):
            stream = StreamConstructor(set_up("data.json", "flow_rate", -5)).stream

    def test_pressure_float(self):
        with pytest.raises(TypeError):
            stream = StreamConstructor(set_up("data.json", "pressure", "hello")).stream

    def test_temperature_float(self):
        with pytest.raises(TypeError):
            stream = StreamConstructor(set_up("data.json", "temperature", "2")).stream

    def test_flow_float(self):
        with pytest.raises(TypeError):
            stream = StreamConstructor(set_up("data.json", "flow_rate", "2")).stream
