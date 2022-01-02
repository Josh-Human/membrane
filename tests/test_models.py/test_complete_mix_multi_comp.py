from new_membrane.models.complete_mix_multi_comp import CompleteMix
from conftest import set_up, set_up_membrane
import pytest

DIR_PATH = "C:\\Users\\jhuma\\OneDrive\Desktop\python\\new-membrane\\tests\\test_data"


class TestCompleteMix:
    membrane_file = "membrane_data.json"
    stream_file = "stream_data.json"

    def test_create_instance(self):
        model = CompleteMix(
            DIR_PATH,
            set_up(self.stream_file),
            set_up(self.stream_file),
            set_up(self.stream_file),
            set_up_membrane(self.membrane_file),
        )
        assert isinstance(model, CompleteMix)


class TestCompleteMixGet:
    membrane_file = "membrane_data.json"
    stream_file = "stream_data.json"
    stream_file_out = "stream_data_out.json"
    permeate_stream_file = "permeate_stream_data.json"

    stream_data_in = {
        "composition": {"A": 0.25, "B": 0.55, "C": 0.2},
        "flow_rate": 10000.0,
        "temperature": 50.0,
        "pressure": 300,
    }
    stream_data_out = {
        "composition": {"A": 0, "B": 0, "C": 0},
        "flow_rate": 10,
        "temperature": 50.0,
        "pressure": 300,
    }
    permeate_stream_data = {
        "composition": {"A": 0, "B": 0, "C": 0},
        "flow_rate": 0,
        "temperature": 50.0,
        "pressure": 30,
    }
    membrane_data = {
        "permeability": {"A": 200e-10, "B": 50e-10, "C": 25e-10},
        "area": 500,
        "dA": 10,
        "thickness": 0.00254,
    }

    model = CompleteMix(
        DIR_PATH,
        set_up(stream_file, "data", stream_data_in),
        set_up(stream_file_out, "data", stream_data_out),
        set_up(permeate_stream_file, "data", permeate_stream_data),
        set_up_membrane(membrane_file, "data", membrane_data),
    )

    def test_get_feed_composition(self):
        assert self.model.feed_composition == {"A": 0.25, "B": 0.55, "C": 0.2}

    def test_get_feed_flow(self):
        assert self.model.feed_flow == 10000

    def test_get_cut(self):
        assert self.model.cut == 0

    def test_get_pl(self):
        assert self.model.pl == 300

    def test_get_ph(self):
        assert self.model.ph == 30

    def test_get_permeabilities(self):
        assert self.model.permeabilities == {"A": 200e-10, "B": 50e-10, "C": 25e-10}

    def test_get_permeate_composition(self):
        assert self.model.permeate_composition == {"A": 0, "B": 0, "C": 0}

    def test_get_thickness(self):
        assert self.model.thickness == 0.00254

    def test_calculate_permeate_composition_returns_correct(self):
        self.model.cut = 0.25
        result = self.model.calculate_permeate_composition(0.5)
        assert result == pytest.approx(-0.1525, 0.001)

    def test_calculate_permeate_composition_calculates_composition(self):
        self.model.cut = 0.25
        self.model.calculate_permeate_composition(0.5)
        assert self.model.permeate_composition == pytest.approx(
            {
                "A": 0.5,
                "B": 0.5366,
                "C": 0.1159,
            },
            0.001,
        )

    def test_calculate_reject_composition_calculates_composition(self):
        self.model.cut = 0.25
        result = self.model.calculate_reject_composition(0.5)
        assert result == pytest.approx(
            {
                "A": 0.1815,
                "B": 0.5833,
                "C": 0.2352,
            },
            0.001,
        )
