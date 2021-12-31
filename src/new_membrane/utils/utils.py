from typing import Union
from numbers import Number as num


def check_values_positive(obj: Union[list, dict]) -> bool:
    if isinstance(obj, list):
        return all(value >= 0 for value in obj)
    return all(v >= 0 for v in iter(obj.values()))


def check_all_values_number(obj: Union[list, dict]) -> bool:
    if isinstance(obj, list):
        return all(isinstance(value, num) for value in obj)
    return all(isinstance(v, num) for v in iter(obj.values()))


def check_and_update(self, attr: str, newValues: Union[list, dict]) -> None:
    """General method to check validity of input & updates a dict attribute.

    Takes a dictionary attribute to update, and a list or dict to update to. Checks are done to ensure values in list and dict are valid and then attribute is updated.
    """
    if not check_values_positive(newValues):
        raise ValueError("New values must be positive")

    if isinstance(newValues, list):
        getattr(self, attr).update(zip(getattr(self, attr), newValues))
    else:
        getattr(self, attr).update(newValues)
