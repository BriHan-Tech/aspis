from typing import Callable, Sequence, TypeVar

from .curry import curry


T = TypeVar("T")
U = TypeVar("U")


@curry
def add_index_right(func: Callable[[T, int], U], arr: Sequence[T]) -> Sequence[U]:
    """
    Maps a function over the reversed sequence, passing both the index and the element to the function.

    Args:
        func : Callable[[T, int], U]
            A function that takes an element and its index as arguments and
            returns a transformed result.

        arr : Sequence[T]
            The sequence to be mapped over.

    Returns:
        Sequence[U]
            A new sequence with the results of the function applied to each element in reverse.
    """

    arr_len = len(arr)
    result_arr = map(lambda x: func(x[1], arr_len - 1 - x[0]), enumerate(reversed(arr)))

    if isinstance(arr, tuple):
        return tuple(result_arr)

    return list(result_arr)
