from pytest import fail

from aspis.common import flip


def test_basic_flip():
    f = lambda x, y: str(x) + str(y)
    flipped_f = flip(f)
    assert flipped_f(1, 2) == "21"

    f = lambda x: str(x)
    flipped_f = flip(f)
    assert flipped_f(1) == "1"


def test_flip_decorator():
    @flip
    def f(x, y):
        return str(x) + str(y)

    assert f(1, 2) == "21"


def test_flip_too_many_args():
    @flip
    def f(x, y):
        return str(x) + str(y)

    try:
        f(1, 2, 3)
        fail()
    except Exception:
        pass


def test_flip_too_few_args():
    @flip
    def f(x, y):
        return str(x) + str(y)

    try:
        f(1)
        fail()
    except Exception:
        pass
