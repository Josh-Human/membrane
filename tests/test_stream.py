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

    def test_get_component_flow(self):
        assert isinstance(self.stream.component_flow("CO2"), float)


class TestStreamSet:
    stream = StreamConstructor("data.json")

    def test_set_components(self):
        self.stream.components = {"CO2": 0.25, "N2": 0.75}
        assert self.stream.components == {"CO2": 0.25, "N2": 0.75}

    def test_set_flow(self):
        self.stream.flow = 200
        assert self.stream.flow == 200

    def test_set_temperature(self):
        self.stream.temperature = 500
        assert self.stream.temperature == 500

    def test_set_pressure(self):
        self.stream.pressure = 150
        assert self.stream.pressure == 150
