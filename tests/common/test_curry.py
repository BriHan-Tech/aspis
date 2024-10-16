from aspis.common import curry


def test_curry_decorator():
    @curry
    def add(a, b, c):
        return a + b + c

    assert add(1)(2)(3) == 6
    assert add(1, 2)(3) == 6
    assert add(1)(2, 3) == 6
    assert add(1, 2, 3) == 6


def test_curry_function():
    def add(a, b, c):
        return a + b + c

    curried_add = curry(add)

    assert curried_add(1)(2)(3) == 6
    assert curried_add(1, 2)(3) == 6
    assert curried_add(1)(2, 3) == 6
    assert curried_add(1, 2, 3) == 6
