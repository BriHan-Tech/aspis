from typing import Callable, cast, List, Sequence, TypeVar

T = TypeVar("T")


def adjust(idx: int, func: Callable[[T], T], seq: Sequence[T]) -> Sequence[T] | str:
    """
    Adjusts the element at the specified index in a sequence by applying a function to it.

    Args:
        idx : int
            The index of the element to adjust. This index must be within the range of the sequence.

        func : Callable[[T], T]
            A function to apply to the element at the specified index.
            It takes the element as input and returns the modified element.

        seq : Sequence[T]
            The sequence (list, tuple, or string) to modify.

    Returns:
        Sequence[T] | str
            A new sequence with the element at the specified index modified.
    """

    if isinstance(seq, str):
        arr = cast(List[T], list(seq))
        arr[idx] = func(arr[idx])
        arr = cast(List[str], arr)
        return "".join(arr)

    new_seq = [*seq]
    new_seq[idx] = func(new_seq[idx])
    return new_seq if isinstance(seq, list) else tuple(new_seq)
