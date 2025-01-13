from functools import partial
from typing import Any, Callable, ParamSpec, TypeVar

from .errors import ArityError
from .utils import error_ctx

P = ParamSpec("P")
T = TypeVar("T")


def eager_partial(fn: Callable[P, T], *args: Any, **kwargs: Any) -> Callable[..., T] | T:
    """
    Partially applies arguments to a function and returns the result immediately if all arguments are provided.
    Otherwise, returns a new function awaiting the rest.

    Note:
    - Over-application is handled by removing arguments from the end
    - Under-application is handled by returning a new function awaiting

    Args:
        fn : Callable[..., T]
            Function to apply arguments to.

        *args : Any
            List of arguments to apply to the function.

        *kwargs : Any
            List of keyword arguments to apply to the function.

    Returns:
        Callable[..., T] | T
            Partially applied function if not all arguments are provided, else the result of the function.
    """

    safe_fn = partial(error_ctx(fn), **kwargs)

    try:
        return safe_fn(*args)
    except ArityError as e:

        # Under Application
        if e.received < e.expected:
            return partial(safe_fn, *args)

        # Over Application
        else:
            for i in range(1, len(args) + 1):
                try:
                    return safe_fn(*args[:-i])
                except ArityError:
                    continue

        raise e
