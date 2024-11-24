from functools import partial
from typing import Any, Callable, ParamSpec, TypeVar

from .errors import ArityError
from .utils import error_ctx

P = ParamSpec("P")
T = TypeVar("T")


def eager_partial(fn: Callable[P, T], *args: Any, **kwargs: Any) -> Callable[..., T] | T:
    """
    Partially applies arguments to a function and returns the result if all arguments are provided.
    Keyword Arguments are always applied.

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

    error_handled_fn = error_ctx(fn)

    try:
        return error_handled_fn(*args, **kwargs)
    except ArityError as e:
        if e.received < e.expected:
            return partial(error_handled_fn, *args, **kwargs)
        raise e
