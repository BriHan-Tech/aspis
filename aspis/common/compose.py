from functools import reduce
from typing import Any, Callable


def compose(*funcs: Callable[..., Any]) -> Callable[..., Any]:
    """
    Performs right-to-left function composition. The last argument may have any arity;
    the remaining arguments must be unary.

    See also pipe

    Args:
        *funcs : Callable[[T], T]
            List of functions to be composed

    Returns:
        Callable
            Right-to-left composed function

    Examples:
        >>> times_two = mutliply(2)
        >>> add_two = add(2)
        >>> multiply_then_add = compose(add_two, times_two)
        >>> result = multiply_then_add(3)  # returns 8
    """

    if not funcs:
        raise ValueError("compose requires at least one function")

    *rest_funcs, last_func = funcs

    return lambda *args: reduce(lambda acc, func: func(acc), reversed(rest_funcs), last_func(*args))
