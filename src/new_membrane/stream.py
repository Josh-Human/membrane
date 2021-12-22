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
    def components(self, newComposition: dict) -> dict:
        self._components = newComposition

    @property
    def flow(self) -> float:
        return self._flow

    @flow.setter
    def flow(self, value) -> None:
        self._flow = value

    @property
    def temperature(self) -> float:
        return self._temperature

    @temperature.setter
    def temperature(self, value) -> None:
        self._temperature = value

    @property
    def pressure(self):
        return self._pressure

    @pressure.setter
    def pressure(self, value) -> None:
        self._pressure = value

    def component_flow(self, component):
        return self._components[component] * self._flow

    @property
    def component_flows(self):
        return self._component_flows

    @component_flows.setter
    def component_flows(self, newFlows: dict) -> dict:
        self._component_flows = newFlows
