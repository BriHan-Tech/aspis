import aspis.common as A


def test_any_all_true():
    assert A.any(lambda x: x > 0, [1, 2, 3, 4, 5]) is True
    assert A.any(lambda x: x > 0)([1, 2, 3, 4, 5]) is True


def test_any_all_false():
    assert A.any(lambda x: x < 0, [1, 2, 3, 4, 5]) is False
    assert A.any(lambda x: x < 0)([1, 2, 3, 4, 5]) is False


def test_curry_mixed_condition():
    assert A.any(lambda x: x > 5, [3, 4, 2, 5]) is False
    assert A.any(lambda x: x > 5)([3, 4, 2, 5]) is False
    assert A.any(lambda x: x > 5)([3, 4, 6, 5]) is True


def test_any_satisfy_with_empty_list():
    assert A.any(lambda x: x > 0)([]) is False
