from aspis.common.curry import curry


@curry
def divide(a: int, b: int) -> float:
    """
    Divides two numbers (a / b).

    Args:
        a : int
            The first number.
        b : int
            The second number.

    Returns:
        float
            The division of the two numbers.

    Examples:
        >>> result = divide(1)(2)  # returns 0.5
    """
    return a / b
