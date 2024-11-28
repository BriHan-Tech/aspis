from typing import Callable, Iterable, TypeVar

from .compose import compose
from .curry import curry

T = TypeVar("T")


@curry
def all_satisfy(pred: Callable[[T], bool], iterable: Iterable[T]) -> bool:
    """
    Returns True if all elements in the iterable satisfy the predicate.

    Args:
        pred : Callable
            The predicate function.

        iterable : Iterable
            The iterable to be tested.

    Returns:
        bool
            True if all elements satisfy the predicate; otherwise, False.
    """
    return compose(all, map)(pred, iterable)
