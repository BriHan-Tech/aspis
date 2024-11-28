from typing import Callable, Iterable, Sequence, TypeVar

from .all import all_satisfy
from .compose import compose
from .curry import curry

T = TypeVar("T")


@curry
def all_pass(preds: Sequence[Callable[[T], bool]], var: T | Iterable[T]) -> bool:
    """
    Checks if all predicates in the given sequence return True when applied to the input variable.

    Args:
        preds : Sequence[Callable[[T], bool]]
            A sequence of predicate functions that take an element of type `T` and return a boolean.

        var : T | Iterable[T]
            The value or iterable of values to test against the predicates.

    Returns:
        bool: True if all predicates return True for the given value or iterable; otherwise, False.

    Example:
        >>> is_positive = lambda x: x > 0
        >>> is_even = lambda x: x % 2 == 0
        >>> all_pass([is_positive, is_even], 4)
        True
        >>> all_pass([is_positive, is_even], -2)
        False

        # With iterables:
        >>> all_pass([lambda x: x > 0, lambda x: x < 10], [1, 2, 3])
        True
        >>> all_pass([lambda x: x > 0, lambda x: x < 10], [1, -2, 3])
        False
    """
    try:
        return compose(all, map)(lambda pred: pred(var), preds)
    except Exception:
        return compose(all, map)(lambda pred: all_satisfy(pred, var), preds)
