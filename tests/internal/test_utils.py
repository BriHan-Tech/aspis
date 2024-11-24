import aspis.internal as Ai


def test_correct_execution():
    fn = lambda a, b: a + b
    result = Ai.error_ctx(fn)(1, 2)
    assert result == 3
