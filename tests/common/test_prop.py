import aspis.common as A


class TestProp:
    x = 1


def test_prop_on_dict():
    # Strings
    assert A.prop("a", {"a": 1, "b": 2}) == 1
    assert A.prop("a", {}) is None
    assert A.prop("a", {"a": [1, 2, 3, 4]}) == [1, 2, 3, 4]

    # Ints
    assert A.prop(1, {1: [1, 2, 3, 4]}) == [1, 2, 3, 4]
    assert A.prop(2, {1: [1, 2, 3, 4]}) is None

    # Missing
    assert A.prop("missing", {"a": 1}) is None
    assert A.prop(42, {1: "one", 2: "two"}) is None

    # Curried
    curried_prop = A.prop("a")
    assert curried_prop({"a": 10}) == 10
    assert curried_prop({"b": 20}) is None


def test_prop_on_class():

    # Static Attrs
    assert A.prop("x", TestProp) == 1
    assert A.prop("missing", TestProp) is None

    # Dynamic Attrs
    obj = TestProp()
    obj.y = 2
    assert A.prop("y", obj) == 2
    assert A.prop("missing", obj) is None

    # @property Attrs
    class TestPropWithProperty:
        @property
        def z(self):
            return 42

    obj_with_property = TestPropWithProperty()
    assert A.prop("z", obj_with_property) == 42
    assert A.prop("missing", obj_with_property) is None


def test_prop_on_invalid():
    assert A.prop("a", 123) is None
    assert A.prop("a", None) is None
    assert A.prop(1, {"a": 1}) is None
    assert A.prop(1, TestProp) is None
