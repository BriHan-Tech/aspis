from functools import wraps
from typing import Callable

from aspis.internal import get_arity


def curry(fn: Callable) -> Callable:
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
    def curried(*args):
        if len(args) >= get_arity(fn):
            return fn(*args)
        return lambda *more_args: curried(*args, *more_args)

    return curried
