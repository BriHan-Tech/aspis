from aspis.common import identity


def test_basic_identity():
    assert identity(2) == 2
    assert identity(lambda x: x + 1)(2) == 3
