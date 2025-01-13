import aspis.common as A


def test_curry_simple_addition():
    add = lambda a, b, c: a + b + c
    curried_add = A.curry(add)

    assert curried_add(1)(2)(3) == 6
    assert curried_add(1, 2)(3) == 6
    assert curried_add(1)(2, 3) == 6
    assert curried_add(1, 2, 3) == 6
    assert curried_add(1, 2, c=3) == 6
    assert curried_add(1, 2)(c=3) == 6
    assert curried_add(c=1)(2)(3) == 6


def test_curry_variadic_function():
    def add(a, *args):
        return a + sum(args)

    curried_add = A.curry(add)

    assert curried_add(1) == 1
    assert curried_add(1, 2) == 3
    assert curried_add(1, 2, 3) == 6


def test_curry_variadic_kwarg_function():
    def add(a, **kwargs):
        return a + sum(kwargs.values())

    curried_add = A.curry(add)

    assert curried_add(1) == 1
    assert curried_add(1, b=2) == 3
    assert curried_add(1, b=2, c=3) == 6


def test_curry_no_arguments():
    def no_args():
        return 42

    curried_no_args = A.curry(no_args)

    assert curried_no_args() == 42


def test_curry_with_default_args():
    def add(a, b, c=10):
        return a + b + c

    curried_add = A.curry(add)
    assert curried_add(1)(2) == 13
    assert curried_add(1, 2) == 13
    assert curried_add(1, 2, 5) == 8


def test_curry_decorator_simple_addition():
    @A.curry
    def add(a: str, b, c):
        return a + b + c

    assert add(1)(2)(3) == 6
    assert add(1, 2)(3) == 6
    assert add(1)(2, 3) == 6
    assert add(1, 2, 3) == 6


def test_curry_should_handle_over_application():
    def add(a, b):
        return a + b

    assert A.curry(add)(1, 2, 3) == 3
    assert A.curry(add)(1)(2, 3) == 3
