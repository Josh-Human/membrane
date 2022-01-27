from typing import Union
from numbers import Number as num
from abc import ABC, abstractmethod


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


class Validator(ABC):
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        pass


class Number(Validator):
    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Expected {value!r} to be an int or float")
        if self.minvalue is not None and value < self.minvalue:
            raise ValueError(f"Expected {value!r} to be at least {self.minvalue!r}")
        if self.maxvalue is not None and value > self.maxvalue:
            raise ValueError(f"Expected {value!r} to be no more than {self.maxvalue!r}")


class PositiveDictionary(Validator):
    def __init__(self):
        pass

    def validate(self, value):
        if not isinstance(value, dict):
            raise TypeError(f"Expected {value!r} to be a dict.")

        if not all(v >= 0 for v in iter(value.values())):
            raise ValueError(f"Expected {value!r} values to be positive.")
