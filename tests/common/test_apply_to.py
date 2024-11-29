import aspis.common as A


def test_apply_to_int():
    assert A.apply_to(1)(lambda x: x + 1) == 2
    assert A.apply_to(1)(lambda x: x + 2) == 3


def test_apply_to_str():
    assert A.apply_to("hello")(lambda s: s + " there") == "hello there"


def test_apply_to_list():
    assert A.apply_to(["hello"])(lambda s: s + ["there"]) == ["hello", "there"]
