import aspis.common as A


def test_aperture_basic():
    assert A.aperture(2, [1, 2, 3, 4, 5]) == [[1, 2], [3, 4]]
    assert A.aperture(2, [1]) == []


def test_aperture_empty_input():
    assert A.aperture(2, []) == []


def test_aperture_n_equal_len():
    assert A.aperture(3, [1, 2, 3]) == [[1, 2, 3]]
    assert A.aperture(1, [1]) == [[1]]


def test_aperture_with_strings():
    assert A.aperture(2, "abcdef") == [["a", "b"], ["c", "d"], ["e", "f"]]


def test_aperture_with_iterators():
    iterator = iter([1, 2, 3, 4, 5])
    assert A.aperture(2, iterator) == [[1, 2], [3, 4]]


def test_aperture_n_zero():
    assert A.aperture(0, [1, 2, 3]) == []


def test_aperture_negative_n():
    assert A.aperture(-1, [1, 2, 3]) == []


def test_aperture_does_not_modify_original_input():
    original = [1, 2, 3, 4]
    A.aperture(2, original)
    assert original == [1, 2, 3, 4]
