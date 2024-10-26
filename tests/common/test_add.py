from pytest import fail

from aspis.common import add


def test_basic_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, -1) == -2
    assert add(-1, 3) == 2


def test_curried_add():
    assert add(2)(3) == 5
    assert add(0)(0) == 0
    assert add(-1)(-1) == -2
    assert add(-1)(3) == 2


def test_error_curried_add():
    try:
        add(-1)(3)(3)
        fail("Should've thrown exception")
    except Exception:
        pass
