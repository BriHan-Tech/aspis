from functools import wraps
from typing import Any, Callable, TypeVar

import aspis.internal as Ai


R = TypeVar("R")


def curry(fn: Callable[..., R]) -> Callable:
    """
    Transforms a function into a curried version.

    Args:
        fn : Callable
            The function to be curried.

    Returns:
        Callable
            A curried version of the original function.

    Examples:
        1. Using `curry` directly:

            >>> def add(a, b, c):
            ...     return a + b + c

            >>> curried_add = curry(add)
            >>> result = curried_add(1)(2)(3)  # returns 6

        2. Using `curry` as a decorator:

            >>> @curry
            ... def multiply(a, b):
            ...     return a * b

            >>> result = multiply(2)(3)  # returns 6
    """

    @wraps(fn)
    def curried(*args: Any, **kwargs: Any) -> Callable | R:
        res = Ai.eager_partial(fn, *args, **kwargs)

        if not callable(res):
            return res

        return lambda *margs, **mkwargs: Ai.eager_partial(res, *margs, **mkwargs)

    return curried
