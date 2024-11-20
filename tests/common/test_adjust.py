import pytest

from aspis.common import adjust


def test_adjust_with_list():
    result = adjust(1, lambda x: x * 2, [1, 2, 3])
    assert result == [1, 4, 3]


def test_adjust_with_tuple():
    result = adjust(0, lambda x: x.upper(), ("hello", "world"))
    assert result == ("HELLO", "world")


def test_adjust_with_string():
    result = adjust(2, lambda x: x.upper(), "hello")
    assert result == "heLlo"


def test_adjust_with_empty_sequence():
    with pytest.raises(IndexError):
        adjust(0, lambda x: x * 2, [])

    with pytest.raises(IndexError):
        adjust(0, lambda x: x.upper(), "")


def test_adjust_with_out_of_bounds_index():
    with pytest.raises(IndexError):
        adjust(10, lambda x: x * 2, [1, 2, 3])

    with pytest.raises(IndexError):
        adjust(5, lambda x: x.upper(), "hi")


def test_adjust_with_negative_index():
    result = adjust(-1, lambda x: x + 1, [1, 2, 3])
    assert result == [1, 2, 4]

    result = adjust(-2, lambda x: x.upper(), "hello")
    assert result == "helLo"
