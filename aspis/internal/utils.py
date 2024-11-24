from functools import wraps
from typing import Callable, ParamSpec, TypeVar

from .errors import ArityError

aspis_errors = {TypeError: ArityError}

R = TypeVar("R")
P = ParamSpec("P")


def error_ctx(fn: Callable[P, R]) -> Callable[P, R]:
    """
    A decorator to handle custom exceptions by mapping them to specific error types.

    Args:
        fn (Callable[P, R]): The function to be wrapped and executed.

    Returns:
        Callable[P, R]: The wrapped function with custom error handling.

    Raises:
        CustomError: A custom error instance based on the `aspis_errors` mapping, if a match is found.
        Exception: The original exception, if no match is found in `aspis_errors`.

    Example:
        >>> @error_ctx
        ... def risky_function():
        ...     raise ValueError("An error occurred")
        ...
        >>> risky_function()  # Raises a custom error if ValueError is mapped in `aspis_errors`.
    """

    @wraps(fn)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        try:
            return fn(*args, **kwargs)
        except Exception as e:
            for error_type, custom_error in aspis_errors.items():
                if isinstance(e, error_type):
                    custom_error_instance = custom_error(e)
                    if custom_error_instance:
                        raise custom_error_instance
            raise e

    return wrapper
