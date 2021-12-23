from typing import Union


class Stream:
    def __init__(
        self, components: dict, flow: float, temp: float, pressure: float
    ) -> None:

        self._components = components
        self._flow = flow
        self._temperature = temp
        self._pressure = pressure
        self._component_flows = dict(
            zip(
                components.keys(),
                [components[component] * self._flow for component in components.keys()],
            )
        )

    @property
    def components(self) -> dict:
        return self._components

    @components.setter
    def components(self, newComposition: Union[dict, list]) -> None:

        if isinstance(newComposition, list):
            if any(value < 0 for value in newComposition):
                raise ValueError("New composition values must be positive")

            self._composition_equals_one(newComposition)
        else:
            if any(v < 0 for v in iter(newComposition.values())):
                raise ValueError("New composition values must be positive")

            self._composition_equals_one(newComposition)

    @property
    def flow(self) -> float:
        return self._flow

    @flow.setter
    def flow(self, value: float) -> None:
        self._flow = value

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
        return self._components[component] * self._flow

    @property
    def component_flows(self):
        return self._component_flows

    @component_flows.setter
    def component_flows(self, newFlows: Union[dict, list]) -> None:
        if isinstance(newFlows, list):
            self._component_flows.update(zip(self._component_flows, newFlows))
        else:
            self._component_flows = newFlows

    def _composition_equals_one(self, newComposition):
        if isinstance(newComposition, list):
            self._components.update(zip(self._components, newComposition))
        else:
            self._components.update(newComposition)

        if sum(self._components.values()) != 1:
            raise ValueError("New composition must equal 1")
