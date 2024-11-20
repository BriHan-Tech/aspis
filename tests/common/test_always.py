import aspis.common as A


def test_always_returns_value():
    always_five = A.always(5)
    assert always_five() == 5

    always_hello = A.always("hello")
    assert always_hello() == "hello"

    always_none = A.always(None)
    assert always_none() is None


def test_always_with_different_types():
    always_list = A.always([1, 2, 3])
    assert always_list() == [1, 2, 3]

    always_dict = A.always({"key": "value"})
    assert always_dict() == {"key": "value"}

    always_tuple = A.always((1, 2, 3))
    assert always_tuple() == (1, 2, 3)


def test_always_return_same_instance():
    obj = [1, 2, 3]
    always_obj = A.always(obj)
    assert always_obj() is obj

    obj_dict = {"key": "value"}
    always_obj_dict = A.always(obj_dict)
    assert always_obj_dict() is obj_dict


def test_always_function_is_callable():
    result = A.always(42)
    assert callable(result)
    assert result() == 42


def test_always_multiple_calls():
    always_ten = A.always(10)
    assert always_ten() == 10
    assert always_ten() == 10
    assert always_ten() == 10
