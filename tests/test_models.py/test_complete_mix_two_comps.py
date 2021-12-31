from new_membrane.models.complete_mix_two_comps import CompleteMixTwo
from conftest import set_up, set_up_membrane

DIR_PATH = "C:\\Users\\jhuma\\OneDrive\Desktop\python\\new-membrane\\tests\\test_data"


class TestCompleteMixTwo:
    membrane_file = "membrane_data.json"
    stream_file = "stream_data.json"

    def test_create_instance(self):
        model = CompleteMixTwo(
            DIR_PATH,
            set_up(self.stream_file),
            set_up(self.stream_file),
            set_up_membrane(self.membrane_file),
        )
        assert isinstance(model, CompleteMixTwo)


class TestCompleteMixTwoGet:
    membrane_file = "membrane_data.json"
    stream_file = "stream_data.json"
    stream_file_out = "stream_data_out.json"
    permeate_stream_file = "permeate_stream_data.json"

    stream_data_in = {
        "composition": {"CO2": 0.5, "N2": 0.5},
        "flow_rate": 100.0,
        "temperature": 50.0,
        "pressure": 80,
    }
    stream_data_out = {
        "composition": {"CO2": 0.25, "N2": 0.75},
        "flow_rate": 0,
        "temperature": 50.0,
        "pressure": 80,
    }
    permeate_stream_data = {
        "composition": {"CO2": 0.1, "N2": 0},
        "flow_rate": 0,
        "temperature": 50.0,
        "pressure": 50,
    }
    membrane_data = {"permeability": {"CO2": 10, "N2": 5}, "area": 500, "dA": 10}

    model = CompleteMixTwo(
        DIR_PATH,
        set_up(stream_file, "data", stream_data_in),
        set_up(stream_file_out, "data", stream_data_out),
        set_up(permeate_stream_file, "data", permeate_stream_data),
        set_up_membrane(membrane_file, "data", membrane_data),
    )

    def test_get_xf(self):
        assert self.model.xf == 0.5

    def test_get_xo(self):
        assert self.model.xo == 0.25

    def test_get_alpha(self):
        assert self.model.alpha == 2

    def test_get_pr(self):
        assert self.model.pr == 1.8
