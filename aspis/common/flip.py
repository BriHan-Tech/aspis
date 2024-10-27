from typing import Any, Callable


def flip(fn: Callable[..., Any]) -> Callable[..., Any]:
    """
    Returns a new function that, when called, invokes `fn` with arguments in reverse order.

    Args:
        fn : Callable[..., Any]
            The function to be called with reversed arguments.

    Returns:
        Callable[..., Any]
            A new function that calls `fn` with reversed arguments.
    """

    def wrapper(*args: Any, **kwargs: Any) -> Callable[..., Any]:
        return fn(*reversed(args), **kwargs)

    return wrapper
