import pytest


class TestMembraneGet:
    def test_get_all_permeabilities(self, membrane):
        assert membrane.permeability == {"CO2": 5, "N2": 5}

    def test_get_single_permeability(self, membrane):
        assert membrane.permeability["CO2"] == 5

    def test_get_invalid_permeability(self, membrane):
        with pytest.raises(KeyError):
            membrane.permeability["H2O"]

    def test_get_area(self, membrane):
        assert membrane.area == 500

    def test_get_no_stages(self, membrane):
        assert membrane.stages == 50

    def test_get_thickness(self, membrane):
        assert membrane.thickness == 0.001


class TestMembraneSet:
    def test_set_permeability_dict(self, membrane):
        membrane.permeability = {"CO2": 0.25, "N2": 0.75}

        assert membrane.permeability == {"CO2": 0.25, "N2": 0.75}

    def test_set_permeability_dict_incorrect_length(self, membrane):

        membrane.permeability = {"CO2": 0.25, "N2": 0.25, "H2O": 0.5}
        membrane.permeability = {"CO2": 0.1, "N2": 0.4}

        assert membrane.permeability == {"CO2": 0.1, "N2": 0.4, "H2O": 0.5}

    def test_set_permeability_list_correct_length(self, membrane):

        membrane.permeability = [0.25, 0.75]

        assert membrane.permeability == {"CO2": 0.25, "N2": 0.75}

    def test_set_permeability_list_incorrect_length(self, membrane):

        membrane.permeability = {"CO2": 0.25, "N2": 0.25, "H2O": 0.5}
        membrane.permeability = [0.1, 0.4]

        assert membrane.permeability == {"CO2": 0.1, "N2": 0.4, "H2O": 0.5}
