from aspis.common import add_index_right


def test_add_index_right_with_list():
    result = add_index_right(lambda val, idx: f"{idx}: {val}", ["a", "b", "c"])
    assert result == ["2: c", "1: b", "0: a"]


def test_add_index_right_with_tuple():
    result = add_index_right(lambda val, idx: val * idx, (2, 3, 4))
    assert result == (8, 3, 0)


def test_add_index_right_with_empty_list():
    result = add_index_right(lambda _, idx: idx, [])
    assert result == []


def test_add_index_right_with_empty_tuple():
    result = add_index_right(lambda _, idx: idx, ())
    assert result == ()


def test_add_index_right_with_non_numeric_elements():
    result = add_index_right(lambda val, idx: (idx, val.upper()), ["hello", "world"])
    assert result == [(1, "WORLD"), (0, "HELLO")]


def test_add_index_right_with_mixed_data_types():
    result = add_index_right(lambda val, idx: (idx, type(val).__name__), [1, "string", 3.5])
    assert result == [(2, "float"), (1, "str"), (0, "int")]
