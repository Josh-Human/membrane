from new_membrane.membrane_constructor import MembraneConstructor
from new_membrane.membrane import Membrane


class TestMembraneConstructor:
    def test_create_instance(self, membrane_constructor):
        assert isinstance(membrane_constructor, MembraneConstructor)

    def test_stream_constructed(self, membrane):
        assert isinstance(membrane, Membrane)
