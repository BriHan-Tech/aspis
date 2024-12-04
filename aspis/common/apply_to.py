from typing import Callable, TypeVar

from .curry import curry

T = TypeVar("T")
R = TypeVar("R")


@curry
def apply_to(val: T, func: Callable[[T], R]) -> R:
    """
    Takes a value and applies a function to it.

    This function is also known as `thrush` combinator.

    Args:
        val : T
            The value to apply the function to.

    Returns
        Callable[Callable[[T], R], R]
            A function that applies the given value to the given function.
    """
    return func(val)
