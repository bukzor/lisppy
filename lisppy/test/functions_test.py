from lisppy.atom import Atom
from lisppy.lists import S
from lisppy.constants import undefined, NIL, T, F
from lisppy import functions

A, B, C, X, Y = (
    Atom('A'), Atom('B'), Atom('C'), Atom('X'), Atom('Y'),
)


def test_atom():
    "section 3c, page 10"
    assert functions.atom(X) is T
    assert functions.atom(S(X, Y)) is F


def test_eq():
    assert functions.eq(X, X) is T
    assert functions.eq(X, A) is F
    assert functions.eq(X, S(X, A)) is undefined


def test_sublis():
    left = functions.sublis(
        S(S(X, S(S(A, B), NIL)),
          S(S(Y, S(S(B, C), NIL)),
            NIL)),
        S(A, S(X, Y)),
    )
    right = S(A, S(S(A, B), S(B, C)))
    assert left == right
