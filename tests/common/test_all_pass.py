import aspis.common as A


def test_all_pass_with_single_value():
    is_positive = lambda x: x > 0
    is_even = lambda x: x % 2 == 0
    assert A.all_pass([is_positive, is_even], 4) is True
    assert A.all_pass([is_positive, is_even], -4) is False
    assert A.all_pass([is_positive, is_even], 3) is False


def test_all_pass_with_iterable():
    is_positive = lambda x: x > 0
    less_than_ten = lambda x: x < 10
    assert A.all_pass([is_positive, less_than_ten], [1, 2, 3]) is True
    assert A.all_pass([is_positive, less_than_ten], (10, 11, 12)) is False
    assert A.all_pass([is_positive, less_than_ten], set([1, 2, -3])) is False
    assert A.all_pass((is_positive, less_than_ten), [1, 2, 3]) is True
    assert A.all_pass(set((is_positive, less_than_ten)), [1, 2, 3]) is True


def test_all_pass_with_empty_predicate_list():
    assert A.all_pass([], 4) is True
    assert A.all_pass([], [1, 2, 3]) is True


def test_all_pass_with_empty_iterable():
    is_positive = lambda x: x > 0
    assert A.all_pass([is_positive], []) is True
    assert A.all_pass([A.always(True)])([]) is True


def test_all_pass_with_multiple_predicates_and_mixed_data():
    is_positive = lambda x: x > 0
    is_odd = lambda x: x % 2 != 0
    assert A.all_pass([is_positive, is_odd], 3) is True
    assert A.all_pass([is_positive, is_odd], 4) is False
    assert A.all_pass([is_positive, is_odd], [1, 3, 5]) is True
    assert A.all_pass([is_positive, is_odd], [1, 2, 3]) is False


def test_all_pass_with_non_numeric_data():
    is_lowercase = lambda x: x.islower()
    starts_with_a = lambda x: x.startswith("a")
    assert A.all_pass([is_lowercase, starts_with_a], "apple") is True
    assert A.all_pass([is_lowercase, starts_with_a], "Apple") is False
    assert A.all_pass([is_lowercase, starts_with_a], ["apple", "art"]) is True
    assert A.all_pass([is_lowercase, starts_with_a], ["apple", "Book"]) is False
