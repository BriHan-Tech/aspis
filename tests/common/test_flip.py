import pytest

import aspis.common as A


def test_basic_flip():
    fn = lambda x, y: str(x) + str(y)
    flipped_fn = A.flip(fn)
    assert flipped_fn(1, 2) == "21"


def test_flip_decorator():
    @A.flip
    def f(x, y):
        return str(x) + str(y)

    assert f(1, 2) == "21"


def test_flip_curried_fn():
    add_str = lambda a, b, c: f"{a}{b}{c}"
    flipped_add_str = A.flip(add_str)
    assert callable(flipped_add_str(1)(2))
    assert flipped_add_str(1)(2)(3) == "213"

    add_str = lambda a, b, *args: f"{a}{b}{sum(args)}"
    flipped_add_str = A.flip(add_str)
    assert flipped_add_str(1)(2, 3, 4, 5) == "2112"


def test_flip_over_application():
    @A.flip
    def f(x, y):
        return str(x) + str(y)

    assert f(1, 2, 3) == "21"


def test_flip_with_keyword_arguments():
    def greet(first_name, last_name):
        return f"Hello, {first_name} {last_name}!"

    with pytest.raises(TypeError):
        A.flip(greet)("Doe", first_name="John")("John")

    def greet_successfully(first_name, last_name, greeting):
        return f"{greeting}, {first_name} {last_name}!"

    assert A.flip(greet_successfully)("Doe", greeting="Hello")("John") == "Hello, John Doe!"


def test_flip_one_argument():
    def single_arg(x):
        return f"Only {x}"

    flipped_single_arg = A.flip(single_arg)

    assert callable(flipped_single_arg(1))

    with pytest.raises(TypeError):
        flipped_single_arg(1)(2)
