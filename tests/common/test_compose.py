from aspis.common import add, compose, divide, identity, multiply


def test_single_function():
    double = lambda x: x * 2
    composed = compose(double)
    assert composed(2) == 4
    assert composed(3) == 6


def test_two_functions():
    double = lambda x: x * 2
    increment = lambda x: x + 1
    composed = compose(double, increment)
    assert composed(2) == 6
    assert composed(3) == 8


def test_multiple_functions():
    assert compose(add(1), multiply(2))(3) == 7
    assert compose(multiply(2), add(1))(3) == 8
    assert compose(multiply(2), add(1), divide(3))(3) == 4


def test_compose_with_multiple_args():
    composed = compose(lambda x: x**2, lambda x, y: x + y)
    assert composed(2, 3) == 25


def test_identity_function():
    composed = compose(identity)
    assert composed(2) == 2
