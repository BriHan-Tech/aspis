from functools import partial
from typing import Any, Callable, ParamSpec, TypeVar

from .errors import ArityError
from .utils import error_ctx

P = ParamSpec("P")
T = TypeVar("T")


def handle_arity_error(error: ArityError, safe_fn: partial[T]) -> partial | T:
    # Under Application
    if error.underapplied:
        return safe_fn

    # Over Application with Keyword Arguments
    elif error.overapplied and error.kwarg_error:
        del safe_fn.keywords[error.unexpected_kwargs.pop()]

        try:
            return safe_fn()
        except ArityError as new_error:
            if new_error.overapplied:
                return handle_arity_error(new_error, safe_fn)
            raise new_error

    # Over Application with Normal Arguments
    elif error.overapplied and not error.kwarg_error:
        original_args = safe_fn.args

        for i in range(1, len(original_args) + 1):
            new_partial = partial(safe_fn.func, *original_args[:-i], **safe_fn.keywords)

            try:
                return new_partial()
            except ArityError as new_error:
                if new_error.overapplied and not new_error.kwarg_error:
                    continue
                if new_error.overapplied and new_error.kwarg_error:
                    return handle_arity_error(new_error, safe_fn)
                raise new_error

    raise error


def eager_partial(fn: Callable[P, T], *args: Any, **kwargs: Any) -> Callable[..., T] | T:
    """
    Partially applies arguments to a function and returns the result immediately if all arguments are provided.
    Otherwise, returns a new function awaiting the rest.

    Note: Keyword Arguments are prioritized over positional arguments.

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

    safe_fn = partial(error_ctx(fn), *args, **kwargs)

    try:
        return safe_fn()
    except ArityError as e:
        return handle_arity_error(e, safe_fn)
