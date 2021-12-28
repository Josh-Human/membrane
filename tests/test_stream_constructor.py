from new_membrane.stream_constructor import StreamConstructor
from new_membrane.stream import Stream
import pytest
from .conftest import set_up

DIR_PATH = "C:\\Users\\jhuma\\OneDrive\Desktop\python\\new-membrane\\tests\\test_data"


class TestStreamConstructor:
    def test_create_instance(self, stream_constructor):
        assert isinstance(stream_constructor, StreamConstructor)

    def test_stream_constructed(self, stream):
        assert isinstance(stream, Stream)


class TestStreamInputs:
    def test_sum_composition(self):
        with pytest.raises(ValueError) as e:
            stream = StreamConstructor(
                DIR_PATH, set_up("data.json", "composition", {"CO2": 0.7, "N2": 0.5})
            ).stream

        assert str(e.value) == "Composition does not sum to 1."

    def test_negative_composition(self):
        with pytest.raises(ValueError) as e:
            stream = StreamConstructor(
                DIR_PATH, set_up("data.json", "composition", {"CO2": -0.25, "N2": 1.25})
            ).stream

        assert str(e.value) == "Composition values should all be positive."

    def test_composition_is_dict(self):
        with pytest.raises(TypeError) as e:
            stream = StreamConstructor(
                DIR_PATH, set_up("data.json", "composition", ["CO2", 0.5, "N2", 0.5])
            ).stream
        assert str(e.value) == "Composition should be type dict."

    def test_composition_values_are_number(self):
        with pytest.raises(TypeError) as e:
            stream = StreamConstructor(
                DIR_PATH, set_up("data.json", "composition", {"CO2": "0.5", "N2": 0.5})
            ).stream

        assert str(e.value) == "Composition values should be Numbers."

    def test_pressure_positive(self):
        with pytest.raises(ValueError) as e:
            stream = StreamConstructor(
                DIR_PATH, set_up("data.json", "pressure", -0.1)
            ).stream

            assert str(e.value) == "Pressure below 0."

    def test_flow_positive(self):
        with pytest.raises(ValueError) as e:
            stream = StreamConstructor(
                DIR_PATH, set_up("data.json", "flow_rate", -5)
            ).stream
        assert str(e.value) == "Flow rate below 0."

    def test_pressure_number(self):
        with pytest.raises(TypeError) as e:
            stream = StreamConstructor(
                DIR_PATH, set_up("data.json", "pressure", "hello")
            ).stream
        assert str(e.value) == "Pressure should be type Number."

    def test_temperature_number(self):
        with pytest.raises(TypeError) as e:
            stream = StreamConstructor(
                DIR_PATH, set_up("data.json", "temperature", "2")
            ).stream
        assert str(e.value) == "Temperature should be type Number."

    def test_flow_number(self):
        with pytest.raises(TypeError) as e:
            stream = StreamConstructor(
                DIR_PATH, set_up("data.json", "flow_rate", "2")
            ).stream
        assert str(e.value) == "Flow rate should be type Number."
