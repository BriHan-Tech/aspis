import aspis.common as A


def test_apply_spec_simple():
    spec = {
        "a": lambda x: x + 1,
        "b": lambda x: x * 2,
    }

    assert A.apply_spec(spec)(5) == {
        "a": 6,
        "b": 10,
    }


def test_apply_spec_nested():
    spec = {
        "a": lambda x, y: x + y,
        "b": {
            "c": lambda: 1,
            "d": lambda x: x * 2,
            "e": lambda _, y: y**2,
        },
    }

    assert A.apply_spec(spec)(2, 3) == {
        "a": 5,
        "b": {"c": 1, "d": 4, "e": 9},
    }


def test_apply_spec_with_kwargs():
    spec = {
        "a": lambda x, prefix="": prefix + str(x),
        "b": lambda x, suffix="": str(x) + suffix,
    }

    assert A.apply_spec(spec)(5, prefix=">", suffix="<") == {
        "a": ">5",
        "b": "5<",
    }


def test_apply_spec_empty_spec():
    spec = {}
    assert A.apply_spec(spec) == {}
    assert A.apply_spec(spec, x=2) == {}
    assert A.apply_spec(spec, 2, 3) == {}


def test_apply_spec_no_callable():
    spec = {
        "a": 42,
        "b": {
            "c": "not a function",
        },
    }

    assert A.apply_spec(spec) == {
        "a": {},
        "b": {
            "c": {},
        },
    }
