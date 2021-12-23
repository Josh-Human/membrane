from new_membrane.membrane_constructor import MembraneConstructor
from new_membrane.stream import Stream
import pytest
from .conftest import set_up


class TestMembraneConstructor:
    def test_create_instance(self, membrane_constructor):
        assert isinstance(membrane_constructor, MembraneConstructor)

    def test_stream_constructed(self, stream):
        assert isinstance(stream, Stream)
