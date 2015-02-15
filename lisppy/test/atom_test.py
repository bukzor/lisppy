from lisppy.atom import Atom

def test_eq():
    x = Atom('x')
    assert x == x
    assert x == Atom('x')
    assert (x == Atom('y')) is not True
    assert (x == 'y') is not True

def test_ne():
    x = Atom('x')
    assert (x != x) is not True
    assert (x != Atom('x')) is not True
    assert x != Atom('y')
    assert x != 'y'


def test_repr():
    for obj in ('foo', u'wat'):
        assert repr(Atom(obj)) == obj
