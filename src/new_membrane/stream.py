from typing import Union
from .utils.utils import check_values_positive


class Stream:
    """Object representing a ChemEng process stream."""

    def __init__(
        self, composition: dict, flow: float, temp: float, pressure: float
    ) -> None:
        """Initialization of Stream object.

        :param _composition: Dictionary representing components and their       respective molar fraction.
        :param _flow: value representing molar flow rate
        :param _temperature: value represnting temperature of stream
        :param _pressure: value representing sream pressure
        :param _component_flows: Dictionary represnting components and their    respective molar flow rates. Initally calculated using total flow and composition.
        """
        self._composition = composition
        self._flow = flow
        self._temperature = temp
        self._pressure = pressure
        self._component_flows = self._initial_component_flow()

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
        self._check_values_and_update("_composition", newComposition)

        if sum(self._composition.values()) != 1:
            raise ValueError("New composition must equal 1")

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
        if value < 0:
            raise ValueError("Flow must be positive")
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
        if value < 0:
            raise ValueError("Pressure must be positive")
        self._pressure = value

    def _initial_component_flow(self) -> dict:
        """Calculates inital component flow rates.

        Takes initial composition and flowrate to calculate component flowrates. getss a dict of component:flowrate.
        """
        return dict(
            zip(
                self._composition.keys(),
                [
                    self._composition[component] * self._flow
                    for component in self._composition.keys()
                ],
            )
        )

    @property
    def component_flows(self) -> dict:
        """
        :getter: get component flows
        :setter: set component flows \n
                 Takes a dictionary or list and sets component flows to values if float and positive. Updates total flow rate and composition to ensure consistency.
        """
        return self._component_flows

    @component_flows.setter
    def component_flows(self, newFlows: Union[dict, list]) -> None:

        self._check_values_and_update("_component_flows", newFlows)

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

    def _check_values_and_update(self, attr: str, newValues: Union[list, dict]) -> None:
        """General method to check validity of input & updates a dict attribute.

        Takes a dictionary attribute to update, and a list or dict to update to. Checks are done to ensure values in list and dict are valid and then attribute is updated.
        """
        if check_values_positive(newValues):
            raise ValueError("New values must be positive")

        if isinstance(newValues, list):
            getattr(self, attr).update(zip(getattr(self, attr), newValues))
        else:
            getattr(self, attr).update(newValues)
