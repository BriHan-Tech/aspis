from collections.abc import Callable, Mapping
from typing import Any

import aspis.internal as Ai

from .curry import curry


def process_mapping(obj: Mapping, fn: Callable) -> Mapping:
    return {k: process_mapping(v, fn) if isinstance(v, Mapping) else fn(v) for k, v in obj.items()}


def has_completed(obj: Mapping) -> bool:
    return not any(
        map(lambda v: (isinstance(v, Mapping) and not has_completed(v)) or isinstance(v, Callable), obj.values())
    )


def nested_apply(obj: Mapping, *args: Any, **kwargs: Any) -> Mapping:
    return process_mapping(obj, lambda v: Ai.eager_partial(v, *args, **kwargs) if isinstance(v, Callable) else v)


def convert_vars(obj: Mapping) -> Mapping:
    return process_mapping(
        obj,
        lambda v: {} if not (isinstance(v, Mapping) or isinstance(v, Callable)) else v,
    )


@curry
def apply_spec(spec: Mapping, *args: Any, **kwargs: Any) -> Mapping | Callable:
    """
    Given a spec object recurisvely mapping properties to functions,
    creates a function producing an object of the same structure,
    by mapping each property to the result of calling its associated function
    with the supplied arguments.

    Args:
        spec : dict
            A dictionary mapping properties to functions

        *args: Any
            The arguments to be passed to the functions

        **kwargs: Any
            The keyword arguments to be passed to the functions

    Returns: Mapping
        An object with the same structure as `spec` where each property is the result
        of calling the associated function with the arguments.
    """
    new_spec = convert_vars(spec)
    new_spec = nested_apply(new_spec, *args, **kwargs)

    if has_completed(new_spec):
        return new_spec

    return lambda *margs, **mkwargs: nested_apply(new_spec, *margs, **mkwargs)
