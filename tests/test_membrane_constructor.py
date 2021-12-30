from new_membrane.components import MembraneConstructor
from new_membrane.components import Membrane
import pytest
from .conftest import set_up_membrane


DIR_PATH = "C:\\Users\\jhuma\\OneDrive\Desktop\python\\new-membrane\\tests\\test_data"


class TestMembraneConstructor:
    def test_create_instance(self, membrane_constructor):
        assert isinstance(membrane_constructor, MembraneConstructor)

    def test_membrane_constructed(self, membrane):
        assert isinstance(membrane, Membrane)


class TestMembraneInputs:
    file = "membrane_data.json"

    def test_negative_permeability(self):
        input = {"CO2": -0.7, "N2": 0.5}
        with pytest.raises(ValueError) as e:
            stream = MembraneConstructor(
                DIR_PATH,
                set_up_membrane(self.file, "permeability", input),
            ).membrane

        assert str(e.value) == "Permeability values should all be positive."

    def test_permeability_is_dict(self):
        input = ["CO2", -0.7, "N2", 0.5]
        with pytest.raises(TypeError) as e:
            stream = MembraneConstructor(
                DIR_PATH,
                set_up_membrane(self.file, "permeability", input),
            ).membrane

        assert str(e.value) == "Permeability should be type dict."

    def test_permeability_values_are_number(self):
        input = {"CO2": "-0.7", "N2": 0.5}
        with pytest.raises(TypeError) as e:
            stream = MembraneConstructor(
                DIR_PATH,
                set_up_membrane(self.file, "permeability", input),
            ).membrane

        assert str(e.value) == "Permeability values should be Numbers."

    def test_negative_area(self):
        input = -200
        with pytest.raises(ValueError) as e:
            stream = MembraneConstructor(
                DIR_PATH,
                set_up_membrane(self.file, "area", input),
            ).membrane

        assert str(e.value) == "Area should be positive."

    def test_area_number(self):
        input = "200"
        with pytest.raises(TypeError) as e:
            stream = MembraneConstructor(
                DIR_PATH,
                set_up_membrane(self.file, "area", input),
            ).membrane

        assert str(e.value) == "Area should be type Number."

    def test_negative_dA(self):
        input = -200
        with pytest.raises(ValueError) as e:
            stream = MembraneConstructor(
                DIR_PATH,
                set_up_membrane(self.file, "dA", input),
            ).membrane

        assert str(e.value) == "dA should be positive."

    def test_dA_number(self):
        input = "200"
        with pytest.raises(TypeError) as e:
            stream = MembraneConstructor(
                DIR_PATH,
                set_up_membrane(self.file, "dA", input),
            ).membrane

        assert str(e.value) == "dA should be type Number."

    def test_dA_smaller_than_area(self):
        input = 505
        with pytest.raises(ValueError) as e:
            stream = MembraneConstructor(
                DIR_PATH,
                set_up_membrane(self.file, "dA", input),
            ).membrane

        assert str(e.value) == "dA should be smaller than area."
