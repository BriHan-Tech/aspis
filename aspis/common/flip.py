from typing import Callable, ParamSpec, TypeVar

from .curry import curry

P = ParamSpec("P")
T = TypeVar("T")


def flip(fn: Callable[..., T]) -> Callable:
    """
    Returns a new function much like the supplied one, except that the first two arguments' order is reversed.

    Args:
        fn : Callable[..., Any]
            The function to be called with the first two arguments reversed.

    Returns:
        Callable[..., Any]
            A new function that calls `fn` with the first two arguments reversed.
    """

    def wrapper(a, b, /, *args, **kwargs) -> T:
        return fn(b, a, *args, **kwargs)

    return curry(wrapper)
