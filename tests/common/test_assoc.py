import pytest

import aspis.common as A


def test_assoc_with_dicts():
    result = A.assoc("a", 1, {})
    assert result == {"a": 1}

    original = {"x": 10}
    new_dict = A.assoc("y", 20, original)
    assert new_dict == {"x": 10, "y": 20}
    assert original == {"x": 10}


def test_assoc_with_objects():
    class TestClass:
        def __init__(self):
            self.name = "Original"

    obj = TestClass()

    updated_obj = A.assoc("age", 25, obj)
    assert updated_obj.age == 25
    assert hasattr(obj, "age") is False

    updated_obj = A.assoc("name", "Updated", obj)
    assert updated_obj.name == "Updated"
    assert obj.name == "Original"

    with pytest.raises(TypeError):
        A.assoc(1, "value", obj)


def test_assoc_with_empty_objects():
    empty_dict = {}
    result = A.assoc("key", "value", empty_dict)
    assert result == {"key": "value"}
    assert empty_dict == {}

    class EmptyClass:
        pass

    empty_obj = EmptyClass()
    updated_obj = A.assoc("new_attr", 100, empty_obj)
    assert updated_obj.new_attr == 100
    assert not hasattr(empty_obj, "new_attr")


def test_assoc_partial_application():
    assoc_a_1 = A.assoc("a", 1)
    result = assoc_a_1({})
    assert result == {"a": 1}

    assoc_a = A.assoc("a")
    assoc_a_1_again = assoc_a(1)
    result = assoc_a_1_again({"b": 2})
    assert result == {"b": 2, "a": 1}


def test_assoc_partial_with_kwargs():
    partial_assoc = A.assoc(k="z")
    result = partial_assoc(v=100)(obj={"x": 42})
    assert result == {"x": 42, "z": 100}


def test_assoc_over_application():
    with pytest.raises(TypeError):
        A.assoc("a", 1, {}, "extra")

    with pytest.raises(TypeError):
        A.assoc("a")("b")({}, "extra")
