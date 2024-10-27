from aspis.common.curry import curry


@curry
def multiply(a: int, b: int) -> int:
    """
    Multiplies two numbers.

    Args:
        a : int
            The first number.
        b : int
            The second number.

    Returns:
        int
            The product of the two numbers.

    Examples:
        >>> result = multiply(1)(2)  # returns 2
    """
    return a * b
