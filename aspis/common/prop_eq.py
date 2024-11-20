from typing import Dict, TypeVar

from .curry import curry

T = TypeVar("T")


@curry
def prop_eq(prop: str, value: T, obj: Dict[str, T]) -> bool:
    """
    Returns a check if the specified property of a dictionary equals the given value.

    Args:
        prop : str
            The key of the property to check in the dictionary.

        value : T
            The value to compare against.

        obj: Dict[str, T]
            The dictionary to check the property

    Returns:
        bool
            returns True if the value of the specified property equals `value`; otherwise, False.

    Example:
        >>> is_name_john = prop_eq("name", "John")
        >>> is_name_john({"name": "John", "age": 30})
        True
        >>> is_name_john({"name": "Doe", "age": 25})
        False
    """

    return obj[prop] == value
