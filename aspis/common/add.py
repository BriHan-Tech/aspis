from .curry import curry


@curry
def add(a: int, b: int) -> int:
    """
    Adds two numbers.

    Args:
        a : int
            The first number.
        b : int
            The second number.

    Returns:
        int
            The sum of the two numbers.

    Examples:
        >>> result = add(1)(2)  # returns 3
    """
    return a + b
