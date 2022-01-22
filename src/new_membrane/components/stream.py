from asyncio.windows_events import NULL
from typing import Union
from new_membrane.utils.utils import check_and_update
from new_membrane.utils.utils import Number, PositiveDictionary


class Stream:
    """Object representing a ChemEng process stream."""

    _composition = PositiveDictionary()
    _flow = Number(0)
    _temperature = Number()
    _pressure = Number(0)
    _component_flows = PositiveDictionary

    def __init__(
        self, composition: dict, flow: float, temp: float, pressure: float
    ) -> None:
        """Initialization of Stream object.

        :param _composition: Dictionary representing components and their       respective molar fraction.
        :param _flow: value representing molar flow rate
        :param _temperature: value representing temperature of stream
        :param _pressure: value representing stream pressure
        :param _component_flows: Dictionary representing components and their respective molar flow rates. Initally calculated using total flow and composition.
        """
        self._composition = composition
        self._flow = flow
        self._temperature = temp
        self._pressure = pressure
        self._component_flows = NULL
        self._update_component_flows()

    @property
    def composition(self) -> dict:
        """
        :getter: gets composition of all components.

        :setter: set composition \n
                 Takes a dictionary or list and sets composition to values if float and positive. Checks that new composition sums to 1. Updates component flows to ensure consistency.
        """
        return self._composition

    @composition.setter
    def composition(self, newComposition: Union[dict, list]) -> None:

        self._composition = newComposition
        self._update_component_flows()

    @property
    def flow(self) -> float:
        """
        :getter: gets total flowrate

        :setter: set total flows rate \n
                 Checks new value is postive and sets flow to it. Updates component flows to ensure consistency
        """
        return self._flow

    @flow.setter
    def flow(self, value: float) -> None:
        self._flow = value
        self._update_component_flows()

    @property
    def temperature(self) -> float:
        """
        :getter: get temperature

        :setter: set temperature
        """
        return self._temperature

    @temperature.setter
    def temperature(self, value: float) -> None:
        self._temperature = value

    @property
    def pressure(self) -> float:
        """
        :getter: get temperature

        :setter: set temperature
        """
        return self._pressure

    @pressure.setter
    def pressure(self, value: float) -> None:
        self._pressure = value

    @property
    def component_flows(self) -> dict:
        """
        :getter: get component flows
        :setter: set component flows \n
                 Takes a dictionary or list and sets component flows to values if float and positive. Updates total flow rate and composition to ensure consistency.
        """
        return self._component_flows

    @component_flows.setter
    def component_flows(self, newFlows: dict) -> None:

        self._component_flows = newFlows
        self._update_flow()
        self._update_composition()

    def _update_component_flows(self) -> None:
        """Calculate new component flows.

        When either composition or total flow is changed this method is called to update component flowrates to ensure consistency.
        """
        self._component_flows = dict(
            zip(
                self._composition.keys(),
                [
                    self._composition[component] * self._flow
                    for component in self._composition.keys()
                ],
            )
        )

    def _update_composition(self) -> None:
        """Calculate new compostion.

        When component flows are changed this method is called to update composition to ensure consistency.
        """
        self._composition = dict(
            zip(
                self._composition.keys(),
                [
                    self._component_flows[component] / self._flow
                    for component in self._component_flows.keys()
                ],
            )
        )

    def _update_flow(self) -> None:
        """Calculate new flowrate.

        When component flows are changed this method is called to update total flow to ensure consistency.
        """
        self._flow = sum(self._component_flows.values())


if __name__ == "__main__":
    pass
