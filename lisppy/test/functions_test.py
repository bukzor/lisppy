from lisppy.atom import Atom
from lisppy.lists import S
from lisppy.constants import undefined, NIL, T, F
from lisppy.functions import(
    atom, eq, car, cdr, cons, ff, subst, equal, null, sublis,
)

A, B, C, X, Y = (
    Atom('A'), Atom('B'), Atom('C'), Atom('X'), Atom('Y'),
)


def test_atom():
    "section 3c1, page 10"
    assert atom(X) is T
    assert atom(S(X, Y)) is F


def test_eq():
    "section 3c2, page 10"
    assert eq(X, X) is T
    assert eq(X, A) is F
    assert eq(X, S(X, A)) is undefined


def test_car():
    "section 3c3, page 11"
    assert car(X) is undefined
    assert car(S(X, A)) is X
    assert car(S(S(X, A), Y)) == S(X, A)


def test_cdr():
    "section 3c4, page 11"
    assert cdr(X) is undefined
    assert cdr(S(X, A)) is A
    assert cdr(S(S(X, A), Y)) is Y


def test_cons():
    "section 3c5, page 11"
    assert cons(X, A) == S(X, A)
    assert cons(S(X, A), Y) == S(S(X, A), Y)


def test_relation():
    "section 3c, page 11"
    assert car(cons(X, Y)) is X
    assert cdr(cons(X, Y)) is Y

    x = S(A, B)
    assert cons(car(x), cdr(x)) == x


def test_ff():
    "section 3d1 page 12"
    assert ff(S(S(A, B), C)) is A


def test_subst():
    "section 3d2 page 12"
    assert subst(S(X, A), B, S(S(A, B), C)) == S(S(A, S(X, A)), C)


def test_equal():
    "section 3d3, page 13"
    assert equal(A, A) is T
    assert equal(A, B) is F
    assert equal(A, S(A, B)) is F

    assert equal(S(A, B), S(A, B)) is T
    assert equal(S(A, B), S(A, A)) is F
    assert equal(S(A, B), S(B, B)) is F
    assert equal(S(A, B), A) is F


def test_null():
    "section 3d3, page 13"
    assert null(NIL) is T
    assert null(X) is F
    assert null(S(X, Y)) is F


def test_sublis():
    left = sublis(
        S(S(X, S(S(A, B), NIL)),
          S(S(Y, S(S(B, C), NIL)),
            NIL)),
        S(A, S(X, Y)),
    )
    right = S(A, S(S(A, B), S(B, C)))
    assert left == right
