from typing import TypeVar

T = TypeVar("T")


def identity(x: T) -> T:
    """
    The identity function.

    Args : T
        The value to be returned.

    Returns : T
        The value passed as an argument.
    """
    return x
