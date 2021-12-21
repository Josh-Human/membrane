from new_membrane.obj_constructors import StreamConstructor
import pytest


class TestStreamGet:
    stream = StreamConstructor("data.json").stream

    def test_get_components(self):
        assert isinstance(self.stream.components, dict)
        assert self.stream.components == {"CO2": 0.5, "N2": 0.5}

    def test_get_flow(self):
        assert isinstance(self.stream.flow, float)
        assert self.stream.flow == 500.1

    def test_get_temperature(self):
        assert isinstance(self.stream.temperature, float)
        assert self.stream.temperature == 50

    def test_get_pressure(self):
        assert isinstance(self.stream.pressure, float)
        assert self.stream.pressure == 1.0

    def test_get_component(self):
        assert isinstance(self.stream.CO2, float)
        assert self.stream.CO2 == 0.5
        with pytest.raises(AttributeError):
            self.stream.H2O


class TestStreamSet:
    def test_set_flow(self):
        stream = StreamConstructor("data.json")
        stream.flow = 200
        assert stream.flow == 200
