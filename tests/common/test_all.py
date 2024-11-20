from itertools import count

import aspis.common as A


def test_basic_usage():
    assert A.all(lambda x: x > 0, [1, 2, 3, 4])
    assert not A.all(lambda x: x > 0, [1, -2, 3, 4])
    assert not A.all(lambda x: x < 0, [1, 2, 3, 4])


def test_partial_application():
    all_positive = A.all(lambda x: x > 0)
    assert all_positive([1, 2, 3])
    assert not all_positive([1, -2, 3])

    all_non_empty = A.all(lambda x: len(x) > 0)
    assert all_non_empty(["hello", "world"])
    assert not all_non_empty(["hello", ""])


def test_with_empty_iterable():
    assert A.all(lambda x: x > 0, [])
    assert A.all(lambda x: len(x) > 0, [])


def test_with_non_numeric_iterables():
    assert A.all(lambda x: x.islower(), ["hello", "world"])
    assert not A.all(lambda x: x.islower(), ["Hello", "world"])

    assert A.all(lambda x: isinstance(x, int), [1, 2, 3])
    assert not A.all(lambda x: isinstance(x, int), [1, "two", 3])


def test_edge_cases():
    assert A.all(lambda x: x > 0, [1])
    assert not A.all(lambda x: x > 0, [-1])

    less_than_ten = A.all(lambda x: x < 10)
    assert not less_than_ten(count(10))
