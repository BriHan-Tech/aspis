from collections.abc import Mapping

from typing import TypeVar

from .curry import curry


T = TypeVar("T")
R = TypeVar("R")


@curry
def prop(p: T, obj: Mapping[T, R] | object) -> R | None:
    """
    Returns the value of property `p` in object `obj` if it exists, otherwise return None

    Args:
        p : T
            The property to be retrieved from the object.

        obj : Mapping[T, R]
            The object to retrieve the property from.

    Returns:
        R | None
            The value of property `p` in object `obj` if it exists, otherwise return None
    """

    if isinstance(obj, Mapping):
        return obj.get(p)

    if isinstance(p, str) and hasattr(obj, p):
        return getattr(obj, p)

    return None
