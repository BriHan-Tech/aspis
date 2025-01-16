from aspis.common import gt


def test_basic_equality():
    assert gt(5, 3)
    assert not gt(2, 3)
    assert not gt(4, 4)
    
    assert gt('z', 'a')
    assert not gt('a', 'z')
    assert not gt('a', 'a')


def test_partial_application():
    gt_five = gt(5)
    assert gt_five(4)
    assert not gt_five(5)
    assert not gt_five(6)

    gt_c = gt('c')
    assert gt_c('a')
    assert not gt_c('c')
    assert not gt_c('d')
