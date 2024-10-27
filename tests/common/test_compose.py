from pytest import fail

from aspis.common import add, compose, divide, multiply


def test_basic_compose():
    assert compose(add(1), multiply(2))(3) == 7
    assert compose(multiply(2), add(1))(3) == 8
    assert compose(multiply(2), add(1), divide(3))(3) == 4


def test_compose_with_last_binary_func():
    merge = lambda x, y: int(str(x) + str(y))
    assert compose(multiply(2), add(1), merge)(5, 5) == (55 + 1) * 2


def test_compose_with_all_binary_func():
    merge = lambda x, y: int(str(x) + str(y))

    try:
        compose(merge, merge, merge, merge)
        fail()
    except Exception:
        pass
