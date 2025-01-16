from aspis.common import gte


def test_basic_equality():
    assert gte(5, 3)
    assert gte(4, 4)
    assert not gte(2, 3)
    
    
    assert gte('z', 'a')
    assert gte('a', 'a')
    assert not gte('a', 'z')
    

def test_partial_application():
    gte_five = gte(5)
    assert gte_five(4)
    assert gte_five(5)
    assert not gte_five(6)

    gte_c = gte('c')
    assert gte_c('a')
    assert gte_c('c')
    assert not gte_c('d')
