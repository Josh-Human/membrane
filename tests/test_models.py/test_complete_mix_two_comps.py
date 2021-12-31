from new_membrane.models.complete_mix_two_comps import CompleteMixTwo
from conftest import set_up, set_up_membrane
import pytest

DIR_PATH = "C:\\Users\\jhuma\\OneDrive\Desktop\python\\new-membrane\\tests\\test_data"


class TestCompleteMixTwo:
    membrane_file = "membrane_data.json"
    stream_file = "stream_data.json"

    def test_create_instance(self):
        model = CompleteMixTwo(
            DIR_PATH,
            set_up(self.stream_file),
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
        "flow_rate": 10,
        "temperature": 50.0,
        "pressure": 80,
    }
    permeate_stream_data = {
        "composition": {"CO2": 0.1, "N2": 0},
        "flow_rate": 0,
        "temperature": 50.0,
        "pressure": 50,
    }
    membrane_data = {
        "permeability": {"CO2": 10, "N2": 5},
        "area": 500,
        "dA": 10,
        "thickness": 0.001,
    }

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
        assert self.model.pr == 0.625

    def test_get_yp(self):
        assert self.model.yp == 0.1

    def test_get_area(self):
        assert self.model.area == 500

    def test_get_cut(self):
        assert self.model.cut == 0

    def test_set_cut(self):
        self.model.cut = 0.5
        assert self.model.cut == 0.5


class TestCompleMixTwoCaseOne:
    membrane_file = "membrane_data.json"
    stream_file = "stream_data.json"
    stream_file_out = "stream_data_out.json"
    permeate_stream_file = "permeate_stream_data.json"

    stream_data_in = {
        "composition": {"CO2": 0.5, "N2": 0.5},
        "flow_rate": 10000.0,
        "temperature": 50.0,
        "pressure": 80,
    }
    stream_data_out = {
        "composition": {"CO2": 0.25, "N2": 0.75},
        "flow_rate": 10,
        "temperature": 50.0,
        "pressure": 80,
    }
    permeate_stream_data = {
        "composition": {"CO2": 0.1, "N2": 0},
        "flow_rate": 0,
        "temperature": 50.0,
        "pressure": 20,
    }
    membrane_data = {
        "permeability": {"CO2": 50e-10, "N2": 5e-10},
        "area": 500,
        "dA": 10,
        "thickness": 0.00254,
    }

    model = CompleteMixTwo(
        DIR_PATH,
        set_up(stream_file, "data", stream_data_in),
        set_up(stream_file_out, "data", stream_data_out),
        set_up(permeate_stream_file, "data", permeate_stream_data),
        set_up_membrane(membrane_file, "data", membrane_data),
    )

    def test_calculate_cut(self):
        assert self.model.calculate_cut() == pytest.approx(0.706, 0.002)

    def test_calculate_area(self):
        self.model.calculate_cut()
        assert self.model.calculate_area() == pytest.approx(273500000, 100000)


class TestCompleMixTwoCaseTwo:
    membrane_file = "membrane_data.json"
    stream_file = "stream_data.json"
    stream_file_out = "stream_data_out.json"
    permeate_stream_file = "permeate_stream_data.json"

    stream_data_in = {
        "composition": {"CO2": 0.209, "N2": 0.791},
        "flow_rate": 1000000.0,
        "temperature": 190.0,
        "pressure": 190,
    }
    stream_data_out = {
        "composition": {"CO2": 0.25, "N2": 0.75},
        "flow_rate": 10,
        "temperature": 50.0,
        "pressure": 190,
    }
    permeate_stream_data = {
        "composition": {"CO2": 0.1, "N2": 0},
        "flow_rate": 0,
        "temperature": 50.0,
        "pressure": 19,
    }
    membrane_data = {
        "permeability": {"CO2": 500e-10, "N2": 50e-10},
        "area": 500,
        "dA": 10,
        "thickness": 0.001,
    }

    model = CompleteMixTwo(
        DIR_PATH,
        set_up(stream_file, "data", stream_data_in),
        set_up(stream_file_out, "data", stream_data_out),
        set_up(permeate_stream_file, "data", permeate_stream_data),
        set_up_membrane(membrane_file, "data", membrane_data),
    )

    def test_calculate_xo(self):
        self.model.cut = 0.2
        assert self.model.calculate_xo() == pytest.approx(0.1346, 0.0005)

    def test_calculate_area(self):
        self.model.cut = 0.2
        self.model.calculate_xo()
        assert self.model.calculate_area() == pytest.approx(322800000, 100000)
