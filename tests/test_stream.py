from new_membrane.obj_constructors import StreamConstructor
import pytest
from .conftest import set_up


class TestStreamGet:
    stream = StreamConstructor(set_up("data.json")).stream

    def test_get_components(self):
        assert self.stream.components == {"CO2": 0.5, "N2": 0.5}

    def test_get_flow(self):
        assert self.stream.flow == 500.1

    def test_get_temperature(self):
        assert self.stream.temperature == 50

    def test_get_pressure(self):
        assert self.stream.pressure == 1.0

    def test_get_component(self):
        assert self.stream.components["CO2"] == 0.5
        with pytest.raises(KeyError):
            self.stream.components["H2O"]

    def test_get_component_flow(self):
        assert self.stream.component_flows["CO2"] == 250.05
        with pytest.raises(KeyError):
            self.stream.components["H2O"]

    def test_get_component_flows(self):
        assert isinstance(self.stream.component_flows, dict)
        assert self.stream.component_flows == {"CO2": 250.05, "N2": 250.05}


class TestStreamSet:
    stream = StreamConstructor(set_up("data.json")).stream

    def test_set_components(self):
        stream = StreamConstructor(set_up("data.json")).stream
        stream.components = {"CO2": 0.25, "N2": 0.75}

        assert stream.components == {"CO2": 0.25, "N2": 0.75}

    def test_set_flow(self):
        stream = StreamConstructor(set_up("data.json")).stream
        stream.flow = 200

        assert stream.flow == 200

    def test_set_temperature(self):
        self.stream.temperature = 500
        assert self.stream.temperature == 500

    def test_set_pressure(self):
        self.stream.pressure = 150
        assert self.stream.pressure == 150
