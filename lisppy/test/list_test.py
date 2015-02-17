import pytest

from lisppy.atom import Atom
from lisppy.lists import S, NIL

m, m1, mn, x = (
    Atom('m'), Atom('m1'), Atom('mn'), Atom('x'),
)


def test_list():
    assert [1, 2, 3] == list(S(1, S(2, S(3, NIL))))


@pytest.mark.parametrize(
    "sexp, abbrev",
    (
        (S(m, NIL), [m]),
        (S(m1, S(mn, NIL)), [m1, mn]),
        (S(m1, S(mn, x)), [m1, S(mn, x)]),
    )
)
def test_abbrev(sexp, abbrev):
    assert sexp.abbreviation == abbrev
