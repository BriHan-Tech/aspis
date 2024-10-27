from functools import reduce
from typing import Any, Callable

from aspis.internal import get_arity


def pipe(first_func: Callable[..., Any], *funcs: Callable[[Any], Any]) -> Callable[..., Any]:
    """
    Performs left-to-right function composition. The first argument may have any arity;
    the remaining arguments must be unary.

    See also compose

    Args:
        first_func: Callable[..., Any]
            First function which can be any arity

        *funcs : Callable[[Any], Any]
            List of functions to be composed

    Returns:
        Callable
            Left-to-right composed function

    Examples:
        >>> times_two = mutliply(2)
        >>> add_two = add(2)
        >>> add_then_multiply = pipe(add_two, times_two)
        >>> result = add_then_multiply(3)  # returns 10
    """

    if any(map(lambda f: get_arity(f) != 1, funcs)):
        raise ValueError("every function except for the last one should be unary")

    return lambda *args: reduce(lambda acc, func: func(acc), funcs, first_func(*args))
