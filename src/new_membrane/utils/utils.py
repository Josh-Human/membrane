from typing import Union
from numbers import Number as num


def check_values_positive(obj: Union[list, dict]) -> bool:
    if isinstance(obj, list):
        return any(value < 0 for value in obj)
    return any(v < 0 for v in iter(obj.values()))


def check_all_values_number(obj: Union[list, dict]) -> bool:
    if isinstance(obj, list):
        return all(isinstance(value, num) for value in obj)
    return all(isinstance(v, num) for v in iter(obj.values()))


# compositions_are_num = all(
#     isinstance(self._data["composition"][component], num)
#     for component in self._data["composition"].keys()
# )
