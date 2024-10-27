from pytest import fail

from aspis.common import multiply


def test_basic_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 0) == 0
    assert multiply(-1, -1) == 1
    assert multiply(-1, 3) == -3


def test_curried_multiply():
    assert multiply(2)(3) == 6
    assert multiply(0)(0) == 0
    assert multiply(-1)(-1) == 1
    assert multiply(-1)(3) == -3


def test_error_curried_multiply():
    try:
        multiply(-1)(3)(3)
        fail("Should've thrown exception")
    except Exception:
        pass
