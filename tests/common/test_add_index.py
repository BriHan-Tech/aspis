from aspis.common import add_index


def test_add_index_with_list():
    result = add_index(lambda val, idx: f"{idx}: {val}", ["a", "b", "c"])
    assert result == ["0: a", "1: b", "2: c"]


def test_add_index_with_tuple():
    result = add_index(lambda val, idx: val * idx, (2, 3, 4))
    assert result == (0, 3, 8)


def test_add_index_with_empty_list():
    result = add_index(lambda val, idx: idx, [])
    assert result == []


def test_add_index_with_empty_tuple():
    result = add_index(lambda val, idx: idx, ())
    assert result == ()


def test_add_index_with_non_numeric_elements():
    result = add_index(lambda val, idx: (idx, val.upper()), ["hello", "world"])
    assert result == [(0, "HELLO"), (1, "WORLD")]


def test_add_index_with_different_data_types():
    result = add_index(lambda val, idx: (idx, type(val).__name__), [1, "string", 3.5])
    assert result == [(0, "int"), (1, "str"), (2, "float")]
