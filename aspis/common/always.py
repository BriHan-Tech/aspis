from typing import Any, Callable


def always(x: Any) -> Callable[[], Any]:
    """
    Returns a function that always returns the same value.

    Args:
        x : Any
            The value to be returned by the function.

    Returns:
        Callable
            A function that always returns the value x.

    """
    return lambda *_, **__: x
