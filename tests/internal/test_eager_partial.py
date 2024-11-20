import pytest

from operator import add

from aspis.internal.eager_partial import eager_partial


def test_eager_partial_no_args():
    assert eager_partial(add)(1, 2) == 3


def test_eager_partial_all_args():
    assert eager_partial(add, 1, 2) == 3


def test_eager_partial_insufficient_args():
    test_add = lambda x, y, z: x + y + z

    res = eager_partial(test_add, 1)
    assert res(2, 3) == 6

    res = eager_partial(test_add, 1, 2)
    assert res(3) == 6


def test_eager_partial_excess_args():
    assert eager_partial(add, 1, 2, 3) == 3


def test_eager_partial_with_varargs():
    assert eager_partial(max, 1, 2, 3, 4, 5) == 5


def test_eager_partial_with_non_arity_error():
    divide = lambda x, y: x / y

    with pytest.raises(ZeroDivisionError):
        eager_partial(divide, 1, 0)


def test_eager_partial_with_c_bindings():
    assert eager_partial(max, 1, 2, 3) == 3
