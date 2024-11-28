from typing import Iterable, List, TypeVar

T = TypeVar("T")


def aperture(n: int, arr: Iterable[T]) -> List[List[T]]:
    """
    Returns a new list containing lists of `n` consecutive elements from the original sequence.

    Args:
        n : int
            The number of elements to include in each sublist.

        arr : Iterable
            The list to extract sublists from.

    Returns:
        list[list]
            A new list containing sublists of `n` consecutive elements from the original list.

    Examples:
        1. Extracting sublists of 2 consecutive elements:

            >>> aperture(2, [1, 2, 3, 4, 5])
            [[1, 2], [2, 3], [3, 4], [4, 5]]
    """

    res: List[List[T]] = []
    window: List[T] = []

    for item in arr:
        window.append(item)

        if len(window) == n:
            res.append(window[:])
            window = []

    return res
