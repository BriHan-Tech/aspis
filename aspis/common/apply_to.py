from typing import Callable, TypeVar

T = TypeVar("T")
R = TypeVar("R")


def apply_to(val: T) -> Callable[[Callable[[T], R]], R]:
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

    def wrapper(func: Callable[[T], R]) -> R:
        return func(val)

    return wrapper
