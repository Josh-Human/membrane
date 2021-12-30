from new_membrane.models.complete_mix_two_comps import CompleteMixTwo
from tests.conftest import set_up_membrane, set_up

DIR_PATH = "C:\\Users\\jhuma\\OneDrive\Desktop\python\\new-membrane\\tests\\test_data"


class TestCompleteMixTwo:
    membrane_file = "membrane_data.json"
    stream_file = "stream_data.json"

    def test_create_instance(self):
        print("Hello")
        model = CompleteMixTwo(
            DIR_PATH,
            set_up(self.stream_file),
            set_up(self.stream_file),
            set_up_membrane(self.membrane_file),
        )
        assert isinstance(model, CompleteMixTwo)
