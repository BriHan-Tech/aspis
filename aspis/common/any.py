from typing import Callable, Sequence, TypeVar

from .curry import curry


T = TypeVar("T")


@curry
def any_satisfy(fn: Callable[[T], bool], arr: Sequence[T]) -> bool:
    """
    Returns True if any element in the array satisfies the predicate.

    Args:
        fn : Callable
            The predicate function.

        arr : Sequence
            The array to be tested.

    Returns:
        bool
            True if any element satisfies the predicate; otherwise, False.
    """
    return any(map(fn, arr))
