from aspis.common import equals


def test_basic_equality():
    assert equals(5, 5)
    assert not equals(5, 3)

    assert equals("hello", "hello")
    assert not equals("hello", "world")


def test_partial_application():
    is_five = equals(5)

    assert is_five(5)
    assert not is_five(3)

    is_hello = equals("hello")
    assert is_hello("hello")
    assert not is_hello("world")


def test_comparing_complex_objects():
    assert equals([1, 2, 3], [1, 2, 3])
    assert not equals([1, 2], [1, 2, 3])

    assert equals({"key": "value"}, {"key": "value"})
    assert not equals({"key": "value"}, {"key": "different"})


def test_edge_cases():
    assert equals(None, None)
    assert not equals(None, "non-none")

    assert equals([], [])
    assert equals((), ())
    assert not equals([], ())
