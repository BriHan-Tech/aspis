from typing import Mapping, TypeVar

from .curry import curry
from .prop import prop

T = TypeVar("T")
R = TypeVar("R")


@curry
def prop_eq(p: T, value: R, obj: Mapping[T, R] | object) -> bool:
    """
    Returns a check if the specified property of an object equals the given value.

    Args:
        prop : T
            The key of the property to check in the object

        value : R
            The value to compare against

        obj: Mapping[T, R] | object
            The object to check the property

    Returns:
        bool
            returns True if the value of the specified property equals `value`; otherwise, False.

    Example:
        >>> is_name_john = prop_eq("name", "John")
        >>> is_name_john({"name": "John", "age": 30})
        True
        >>> is_name_john({"name": "Doe", "age": 25})
        False
    """

    return prop(p, obj) == value
