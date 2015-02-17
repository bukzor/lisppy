from lisppy.atom import Atom
from lisppy.lists import S
from lisppy.constants import undefined, NIL
from lisppy.functions import (
    eq, sublis
)

A, B, C, X, Y = (
    Atom('A'), Atom('B'), Atom('C'), Atom('X'), Atom('Y'),
)


def test_eq():
    assert eq(X, X) == True
    assert eq(X, A) == False
    assert eq(X, S(X, A)) == undefined


def test_sublis():
    left = sublis(
        S(S(X, S(S(A, B), NIL)),
          S(S(Y, S(S(B, C), NIL)),
            NIL)),
        S(A, S(X, Y)),
    )
    right = S(A, S(S(A, B), S(B, C)))
    assert left == right
