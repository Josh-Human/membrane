from new_membrane.utils.utils import check_and_update


class Membrane:
    """Object representing a membrane."""

    def __init__(
        self,
        permeability: dict = None,
        area: float = None,
        dA: float = None,
        thickness: float = None,
    ):
        """Initialization of Membrane object.

        :param _permeability: Dictionary representing components and their       respective permeability.
        :param _are: value representing total membrane area
        :param _dA: value representing area step for simulation
        :param _no_stages: Float represnting the total number of stages for simulation. Calculated using total area / dA.
        """
        self._permeability = permeability
        self._area = area
        self._dA = dA
        self._no_stages = area / dA
        self._thickness = thickness

    @property
    def permeability(self):
        """
        :getter: gets permeability of all components.

        :setter: set permeability \n
                 Takes a dictionary or list and sets permeability to values if float and positive.
        """
        return self._permeability

    @permeability.setter
    def permeability(self, newPermeability):
        check_and_update(self, "_permeability", newPermeability)

    @property
    def area(self):
        """
        :getter: gets total area
        :setter: set total area
        """
        return self._area

    @area.setter
    def area(self, value):
        self._area = value

    @property
    def stages(self):
        """
        :getter: gets number of stages
        """
        return self._no_stages

    @property
    def thickness(self):
        """
        :getter: gets membrane thickness
        """
        return self._thickness


if __name__ == "__main__":
    pass
