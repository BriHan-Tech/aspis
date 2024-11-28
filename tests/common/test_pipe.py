from aspis.common import add, divide, identity, multiply, pipe


def test_single_function():
    double = lambda x: x * 2
    piped = pipe(double)
    assert piped(2) == 4
    assert piped(3) == 6


def test_two_functions():
    double = lambda x: x * 2
    increment = lambda x: x + 1
    piped = pipe(double, increment)
    assert piped(2) == 5
    assert piped(3) == 7


def test_multiple_functions():
    assert pipe(add(1), multiply(2))(3) == 8
    assert pipe(multiply(2), add(1))(3) == 7
    assert pipe(multiply(2), add(1), divide(15))(7) == 1


def test_pipe_with_multiple_args():
    piped = pipe(lambda x, y: x + y, lambda x: x**2)
    assert piped(2, 3) == 25


def test_identity_function():
    piped = pipe(identity)
    assert piped(2) == 2
