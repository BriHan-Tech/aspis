from copy import deepcopy
from typing import TypeVar, Mapping

from .curry import curry

T = TypeVar("T")
R = TypeVar("R")


@curry
def assoc(k: T, v: R, obj: Mapping[T, R] | object) -> object:
    """
    Associates a value with a key in an object.

    Args:
        k : Hashable
            The key to associate the value with.

        v : Any
            The value to associate with the key.

        obj : dict
            The object to associate the value with the key.
    """
    if isinstance(obj, dict):
        return {**obj, k: v}

    if not isinstance(k, str):
        raise TypeError(f"Attribute name must be a string when modifying an object, got {type(k)}")

    obj_copy = deepcopy(obj)
    setattr(obj_copy, k, v)
    return obj_copy
