from new_membrane.membrane import Membrane
from new_membrane.obj_constructors import StreamConstructor, MembraneConstructor
from new_membrane.stream import Stream

class TestStreamConstructor:
    streamConstructor = StreamConstructor('data.json')

    def test_create_instance(self):
        assert isinstance(self.streamConstructor, StreamConstructor)
    
    def test_stream_constructed(self):
        assert isinstance(self.streamConstructor.stream, Stream)
    
    def test_get_stream(self):
        assert self.streamConstructor.stream == self.streamConstructor.getStream()

class TestMembraneConstructor:
    membraneConstructor = MembraneConstructor('data.json')

    def test_create_instance(self):
        assert isinstance(self.membraneConstructor, MembraneConstructor)
    
    def test_membrane_constructed(self):
        assert isinstance(self.membraneConstructor.membrane, Membrane)
    
    def test_get_membrane(self):
        assert self.membraneConstructor.membrane == self.membraneConstructor.getMembrane()