from typing import TypeVar

T = TypeVar("T")


def identity(x: T) -> T:
    """
    The identity function.

    Args:
        x : T
            The value to be returned.

    Returns:
        T
            The value passed as an argument.
    """
    return x
