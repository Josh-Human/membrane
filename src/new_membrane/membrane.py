from .utils.utils import check_and_update


class Membrane:
    def __init__(self, permeability: dict, area: float, dA: float):
        self._permeability = permeability
        self._area = area
        self._dA = dA
        self._no_stages = area / dA

    @property
    def permeability(self):
        return self._permeability

    @permeability.setter
    def permeability(self, newPermeability):
        check_and_update(self, "_permeability", newPermeability)

    @property
    def area(self):
        return self._area

    @property
    def stages(self):
        return self._no_stages
