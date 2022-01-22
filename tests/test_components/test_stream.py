import pytest


class TestStreamSet:
    def test_set_composition_updates_component_flows(self, stream):
        stream.composition = {"CO2": 0.25, "N2": 0.75}

        assert stream.component_flows == {"CO2": 125, "N2": 375}

    def test_set_flow_updates_component_flows(self, stream):
        stream.flow = 200

        assert stream.component_flows == {"CO2": 100, "N2": 100}

    def test_set_component_flows_updates_composition(self, stream):
        stream.component_flows = {"CO2": 20, "N2": 30}

        assert stream.composition == {"CO2": 0.4, "N2": 0.6}

    def test_set_component_flows_updates_flow(self, stream):
        stream.component_flows = {"CO2": 20, "N2": 30}

        assert stream.flow == 50

    class TestStreamSetInvalidValues:
        def test_set_composition_has_positive_values(self, stream):

            with pytest.raises(ValueError):
                stream.composition = {"CO2": -0.2, "N2": 0.8}

        def test_set_pressure_has_positive_value(self, stream):

            with pytest.raises(ValueError):
                stream.pressure = -1

        def test_set_component_flows_have_positive_values(self, stream):

            with pytest.raises(ValueError):
                stream.component_flows = {"CO2": -5, "N2": 10}

        def test_set_flow_has_positive_values(self, stream):

            with pytest.raises(ValueError):
                stream.flow = -100
