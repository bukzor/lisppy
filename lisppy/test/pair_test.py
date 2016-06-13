import pytest

from lisppy.atom import Atom
from lisppy.pair import Pair, NIL

m, m1, mn, x = (
    Atom('m'), Atom('m1'), Atom('mn'), Atom('x'),
)


def test_list():
    assert [1, 2, 3] == list(Pair(1, Pair(2, Pair(3, NIL))))


@pytest.mark.parametrize(
    "sexp, abbrev",
    (
        (Pair(m, NIL), [m]),
        (Pair(m1, Pair(mn, NIL)), [m1, mn]),
        (Pair(m1, Pair(mn, x)), Pair(m1, Pair(mn, x))),
    )
)
def test_abbrev(sexp, abbrev):
    assert sexp.abbreviation == abbrev
