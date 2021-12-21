from new_membrane.obj_constructors import StreamConstructor
from new_membrane.stream import Stream

class TestStreamConstructor:
    streamConstructor = StreamConstructor('data.json')

    def test_create_instance(self):
        assert isinstance(self.streamConstructor, StreamConstructor)
    
    def test_stream_constructed(self):
        assert isinstance(self.streamConstructor.stream, Stream)
    



