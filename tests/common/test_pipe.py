from aspis.common import add, divide, multiply, pipe


def test_basic_pipe():
    assert pipe(add(1), multiply(2))(3) == 8
    assert pipe(multiply(2), add(1))(3) == 7
    assert pipe(multiply(2), add(1), divide(3))(3) == 3 / 7


def test_pipe_with_last_binary_func():
    merge = lambda x, y: int(str(x) + str(y))
    assert pipe(merge, add(1), multiply(2))(5, 5) == (55 + 1) * 2
