from lisppy.atom import Atom
from lisppy.constants import undefined, NIL, T, F
from lisppy.functions import(
    atom, eq, car, cdr, cons, ff, subst, equal, null, list_, append, sublis,
)

A, B, C, X, Y = (
    Atom('A'), Atom('B'), Atom('C'), Atom('X'), Atom('Y'),
)


def test_atom():
    "section 3c1, page 10"
    assert atom(X) is T
    assert atom(cons(X, Y)) is F


def test_eq():
    "section 3c2, page 10"
    assert eq(X, X) is T
    assert eq(X, A) is F
    assert eq(X, cons(X, A)) is undefined


def test_car():
    "section 3c3, page 11"
    assert car(X) is undefined
    assert car(cons(X, A)) is X
    assert car(cons(cons(X, A), Y)) == cons(X, A)


def test_cdr():
    "section 3c4, page 11"
    assert cdr(X) is undefined
    assert cdr(cons(X, A)) is A
    assert cdr(cons(cons(X, A), Y)) is Y


def test_cons():
    "section 3c5, page 11"
    assert cons(X, A) == cons(X, A)
    assert cons(cons(X, A), Y) == cons(cons(X, A), Y)


def test_relation():
    "section 3c, page 11"
    assert car(cons(X, Y)) is X
    assert cdr(cons(X, Y)) is Y

    x = cons(A, B)
    assert cons(car(x), cdr(x)) == x


def test_ff():
    "section 3d1 page 12"
    assert ff(cons(cons(A, B), C)) is A


def test_subst():
    "section 3d2 page 12"
    assert subst(cons(X, A), B, cons(cons(A, B), C)) == cons(cons(A, cons(X, A)), C)


def test_equal():
    "section 3d3, page 13"
    assert equal(A, A) is T
    assert equal(A, B) is F
    assert equal(A, cons(A, B)) is F

    assert equal(cons(A, B), cons(A, B)) is T
    assert equal(cons(A, B), cons(A, A)) is F
    assert equal(cons(A, B), cons(B, B)) is F
    assert equal(cons(A, B), A) is F


def test_null():
    "section 3d3, page 13"
    assert null(NIL) is T
    assert null(X) is F
    assert null(cons(X, Y)) is F


def test_list_():
    """page 14"""
    assert list_(A, B, C) == cons(A, cons(B, cons(C, NIL)))
    assert list_(A) == cons(A, NIL)
    assert list_() is NIL


def test_append():
    """section 3d1(again), page 14"""
    assert append(list_(A, B), list_(C, X, Y)) == list_(A, B, C, X, Y)
    assert append(NIL, X) is X


def test_sublis():
    """section 3d5(again), page 15"""
    left = sublis(
        list_(
            list_(X, list_(A, B)),
            list_(Y, list_(B, C)),
        ),
        # the paper shows a list here, where a pair is needed
        cons(A, cons(X, Y)),
    )
    right = list_(A, list_(A, B), B, C)
    assert left == right
