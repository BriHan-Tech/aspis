from pytest import fail

from aspis.common import divide


def test_basic_divide():
    assert divide(2, 3) == 2 / 3
    assert divide(-1, -1) == 1
    assert divide(-1, 3) == -1 / 3


def test_curried_divide():
    assert divide(2)(3) == 2 / 3
    assert divide(-1)(-1) == 1
    assert divide(-1)(3) == -1 / 3


def test_divide_by_zero():
    try:
        divide(1)(0)
        fail("Should've thrown exception")
    except Exception:
        pass


def test_error_curried_divide():
    try:
        divide(-1)(3)(3)
        fail("Should've thrown exception")
    except Exception:
        pass
