import aspis.common as A


class TestObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


def test_prop_eq_with_valid_key():
    is_active = A.prop_eq("status", "active")
    assert is_active({"status": "active", "id": 1}) is True
    assert is_active({"status": "inactive", "id": 2}) is False
    assert is_active(TestObject(status="active", id=1)) is True
    assert is_active(TestObject(status="inactive", id=2)) is False


def test_prop_eq_with_nested_object():
    get_age_30 = A.prop_eq("age", 30)
    assert get_age_30({"age": 30, "name": "Alice"}) is True
    assert get_age_30({"age": 25, "name": "Bob"}) is False
    assert get_age_30(TestObject(age=30, name="Alice")) is True
    assert get_age_30(TestObject(age=25, name="Bob")) is False


def test_prop_eq_with_different_value_types():
    is_price_100 = A.prop_eq("price", 100)
    assert is_price_100({"price": 100, "product": "apple"}) is True
    assert is_price_100({"price": "100", "product": "banana"}) is False
    assert is_price_100(TestObject(price=100, product="apple")) is True
    assert is_price_100(TestObject(price="100", product="banana")) is False

    is_name_empty = A.prop_eq("name", "")
    assert is_name_empty({"name": "", "id": 1}) is True
    assert is_name_empty({"name": "John", "id": 2}) is False
    assert is_name_empty(TestObject(name="", id=1)) is True
    assert is_name_empty(TestObject(name="John", id=2)) is False


def test_prop_eq_partial_match():
    is_id_5 = A.prop_eq("id", 5)
    assert is_id_5({"id": 5, "name": "John", "status": "active"}) is True
    assert is_id_5({"id": 3, "name": "Jane", "status": "inactive"}) is False
    assert is_id_5(TestObject(id=5, name="John", status="active")) is True
    assert is_id_5(TestObject(id=3, name="Jane", status="inactive")) is False


def test_prop_eq_with_nonexistent_property():
    is_anything = A.prop_eq("anything", "value")
    assert is_anything({}) is False
    assert is_anything(TestObject()) is False


def test_prop_eq_case_sensitivity():
    is_status_active = A.prop_eq("status", "Active")
    assert is_status_active({"status": "active"}) is False
    assert is_status_active({"status": "Active"}) is True
    assert is_status_active(TestObject(status="active")) is False
    assert is_status_active(TestObject(status="Active")) is True
