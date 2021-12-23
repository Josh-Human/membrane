from typing import Union


class Stream:
    def __init__(
        self, composition: dict, flow: float, temp: float, pressure: float
    ) -> None:

        self._composition = composition
        self._flow = flow
        self._temperature = temp
        self._pressure = pressure
        self._component_flows = self._update_component_flows()

    @property
    def composition(self) -> dict:
        return self._composition

    @composition.setter
    def composition(self, newComposition: Union[dict, list]) -> None:

        if isinstance(newComposition, list):
            if any(value < 0 for value in newComposition):
                raise ValueError("New composition values must be positive")

            self._composition_equals_one(newComposition)
        else:
            if any(v < 0 for v in iter(newComposition.values())):
                raise ValueError("New composition values must be positive")

            self._composition_equals_one(newComposition)

        self._component_flows = self._update_component_flows()

    @property
    def flow(self) -> float:
        return self._flow

    @flow.setter
    def flow(self, value: float) -> None:
        self._flow = value
        self._component_flows = self._update_component_flows()

    @property
    def temperature(self) -> float:
        return self._temperature

    @temperature.setter
    def temperature(self, value: float) -> None:
        self._temperature = value

    @property
    def pressure(self) -> float:
        return self._pressure

    @pressure.setter
    def pressure(self, value: float) -> None:
        self._pressure = value

    def component_flow(self, component):
        return self._composition[component] * self._flow

    @property
    def component_flows(self):
        return self._component_flows

    @component_flows.setter
    def component_flows(self, newFlows: Union[dict, list]) -> None:
        if isinstance(newFlows, list):
            if any(value < 0 for value in newFlows):
                raise ValueError("New composition values must be positive")

            self._component_flows.update(zip(self._component_flows, newFlows))
        else:
            if any(v < 0 for v in iter(newFlows.values())):
                raise ValueError("New composition values must be positive")
            self._component_flows.update(newFlows)
        self._update_flow()
        self._update_composition()

    def _composition_equals_one(self, newComposition):
        if isinstance(newComposition, list):
            self._composition.update(zip(self._composition, newComposition))
        else:
            self._composition.update(newComposition)

        if sum(self._composition.values()) != 1:
            raise ValueError("New composition must equal 1")

    def _update_component_flows(self):
        return dict(
            zip(
                self._composition.keys(),
                [
                    self._composition[component] * self._flow
                    for component in self._composition.keys()
                ],
            )
        )

    def _update_composition(self):
        self._composition = dict(
            zip(
                self._composition.keys(),
                [
                    self._component_flows[component] / self._flow
                    for component in self._component_flows.keys()
                ],
            )
        )

    def _update_flow(self):
        self._flow = sum(self._component_flows.values())
