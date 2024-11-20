from typing import Callable, Sequence, TypeVar

from .curry import curry

T = TypeVar("T")
U = TypeVar("U")


@curry
def add_index(func: Callable[[T, int], U], arr: Sequence[T]) -> Sequence[U]:
    """
    Maps a function over a sequence, passing the index as a second argument,
    allowing the map function to have access to the index of the element being processed.

    Args:
        func : Callable[[T, int], U]
            A function that takes an element and its index as arguments and
            returns a transformed result.

        arr : Sequence[T]
            The sequence to be mapped over.

    Returns:
        Sequence[U]
            A new sequence with the results of the function applied to each element.
    """
    result_arr = map(lambda x: func(x[1], x[0]), enumerate(arr))

    if isinstance(arr, tuple):
        return tuple(result_arr)

    return list(result_arr)
