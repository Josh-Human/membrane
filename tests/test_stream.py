from new_membrane.obj_constructors import StreamConstructor
import pytest
from .conftest import set_up


@pytest.fixture(autouse=True)
def stream():
    new_stream = StreamConstructor(set_up("data.json")).stream
    print("invoked")
    return new_stream


class TestStreamGet:
    def test_get_composition(self, stream):
        assert stream.composition == {"CO2": 0.5, "N2": 0.5}

    def test_get_flow(self, stream):
        assert stream.flow == 500.0

    def test_get_temperature(self, stream):
        assert stream.temperature == 50

    def test_get_pressure(self, stream):
        assert stream.pressure == 1.0

    def test_get_component(self, stream):
        assert stream.composition["CO2"] == 0.5
        with pytest.raises(KeyError):
            stream.composition["H2O"]

    def test_get_component_flow(self, stream):
        assert stream.component_flows["CO2"] == 250.0
        with pytest.raises(KeyError):
            stream.composition["H2O"]

    def test_get_component_flows(self, stream):
        assert isinstance(stream.component_flows, dict)
        assert stream.component_flows == {"CO2": 250.0, "N2": 250.0}


class TestStreamSet:
    def test_set_composition_dict(self, stream):
        stream.composition = {"CO2": 0.25, "N2": 0.75}

        assert stream.composition == {"CO2": 0.25, "N2": 0.75}

    def test_set_composition_dict_incorrect_length(self, stream):

        stream.composition = {"CO2": 0.25, "N2": 0.25, "H2O": 0.5}
        stream.composition = {"CO2": 0.1, "N2": 0.4}

        assert stream.composition == {"CO2": 0.1, "N2": 0.4, "H2O": 0.5}

    def test_set_composition_list_correct_length(self, stream):

        stream.composition = [0.25, 0.75]

        assert stream.composition == {"CO2": 0.25, "N2": 0.75}

    def test_set_composition_list_incorrect_length(self, stream):

        stream.composition = {"CO2": 0.25, "N2": 0.25, "H2O": 0.5}
        stream.composition = [0.1, 0.4]

        assert stream.composition == {"CO2": 0.1, "N2": 0.4, "H2O": 0.5}

    def test_set_flow_dict(self, stream):
        stream.flow = 200

        assert stream.flow == 200

    def test_set_flows_list_correct_length(self, stream):

        stream.component_flows = [1, 2.5]

        assert stream.component_flows == {"CO2": 1, "N2": 2.5}

    # def test_set_flows_list_incorrect_length(self, stream):

    #     stream.composition = {"CO2": 0.25, "N2": 0.25, "H2O": 0.5}
    #     stream.component_flows = [3, 4]

    #     assert stream.component_flows == {"CO2": 3, "N2": 4, "H2O": 250.0}

    def test_set_temperature(self, stream):
        stream.temperature = 500
        assert stream.temperature == 500

    def test_set_pressure(self, stream):
        stream.pressure = 150
        assert stream.pressure == 150

    class TestStreamSetConsistency:
        def test_set_composition_sums_to_one(self, stream):

            with pytest.raises(ValueError):
                stream.composition = {"CO2": 0.2, "N2": 0.75}

        def test_set_composition_has_positive_values(self, stream):

            with pytest.raises(ValueError):
                stream.composition = {"CO2": -0.2, "N2": 0.8}

        def test_set_composition_updates_component_flows(self, stream):

            with pytest.raises(ValueError):
                stream.composition = {"CO2": -0.2, "N2": 0.8}
