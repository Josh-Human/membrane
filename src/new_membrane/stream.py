class Stream:
    def __init__(
        self, components: dict, flow: float, temp: float, pressure: float
    ) -> None:
        self._components = components
        self._flow = float(flow)
        self._temperature = float(temp)
        self._pressure = float(pressure)

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


    def __getattr__(self, component: str) -> float:
        try:
            return self._components[component]
        except KeyError:
            msg = "'{0}' object has no attribute '{1}'"
            raise AttributeError(msg.format(type(self).__name__, component))

    def component_flow(self, component):
        return self._components[component] * self._flow

    def component_flows(self):
        return [
            self._components[component] * self._flow
            for component in self._components.keys()
        ]
