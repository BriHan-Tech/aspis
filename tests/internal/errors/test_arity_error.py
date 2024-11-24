import pytest

import aspis.internal as Ai
from aspis.internal.errors.arity_error import ArityError


def test_arity_error_missing_args():
    fn = lambda a, b: a

    # should raise arity error
    with pytest.raises(Ai.ArityError) as exc_info:
        Ai.error_ctx(fn)(1)

    assert exc_info.value.is_arity_error
    assert exc_info.value.expected > exc_info.value.received

    # arity error should be a TypeError
    assert isinstance(exc_info.value, TypeError)

    with pytest.raises(TypeError) as type_error:
        fn(1)

    assert str(exc_info.value) == str(type_error.value)


def test_arity_error_extra_args():
    fn = lambda a: a

    # should raise arity error
    with pytest.raises(Ai.ArityError) as exc_info:
        Ai.error_ctx(fn)(1, 2)

    assert exc_info.value.is_arity_error
    assert exc_info.value.expected < exc_info.value.received

    # arity error should be a TypeError
    assert isinstance(exc_info.value, TypeError)

    with pytest.raises(TypeError) as type_error:
        fn(1, 2)
    assert str(exc_info.value) == str(type_error.value)


def test_arity_error_unrelated_error():
    def raise_unrelated_type_error():
        raise TypeError("Unrelated error")

    def raise_unrelated_value_error():
        raise ValueError("Unrelated error")

    with pytest.raises(TypeError) as exc_info:
        Ai.error_ctx(raise_unrelated_type_error)()

    assert not isinstance(exc_info.value, ArityError)
    assert str(exc_info.value) == "Unrelated error"

    with pytest.raises(ValueError) as exc_info:
        Ai.error_ctx(raise_unrelated_value_error)()

    assert not isinstance(exc_info.value, ArityError)
    assert str(exc_info.value) == "Unrelated error"
