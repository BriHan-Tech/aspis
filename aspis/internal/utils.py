import inspect
from typing import Any, Callable


def get_arity(fn: Callable[..., Any]) -> int:
    signature = inspect.signature(fn)
    params = signature.parameters
    return len(params)
