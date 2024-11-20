from functools import partial
from typing import Any, Callable, TypeVar

from aspis.internal.utils import ArityError

T = TypeVar("T")


def eager_partial(fn: Callable[..., T], *bound_args: Any) -> Callable[..., T] | T:
    """
    Partially applies arguments to a function and returns the result if all arguments are provided.
    - Handles under-application with partial application
    - Handles over-application by ignoring excess arguments

    Args:
        fn : Callable[..., T]
            Function to apply arguments to.

        *bound_args : Any
            List of arguments to apply to the function.

    Returns:
        Callable[..., T] | T
            Partially applied function if not all arguments are provided, else the result of the function.

    """

    if len(bound_args) == 0:
        try:
            return fn()
        except TypeError as e:
            arity_error = ArityError(e)

            if not arity_error:
                raise e

            if arity_error.received < arity_error.expected:
                return partial(fn, *bound_args)

    for i in range(len(bound_args), 0, -1):
        try:
            return fn(*bound_args[:i])

        except TypeError as e:
            arity_error = ArityError(e)

            if not arity_error:
                raise e

            if arity_error.received < arity_error.expected:
                return partial(fn, *bound_args)

    return partial(fn, *bound_args)
