from typing import Union


def check_values_positive(obj: Union[list, dict]) -> bool:
    if isinstance(obj, list):
        return any(value < 0 for value in obj)
    return any(v < 0 for v in iter(obj.values()))
