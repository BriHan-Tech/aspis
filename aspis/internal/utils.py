import inspect
from typing import Any, Callable


def num_params(fn: Callable[..., Any]) -> int:
    signature = inspect.signature(fn)
    params = signature.parameters
    return len(params)
