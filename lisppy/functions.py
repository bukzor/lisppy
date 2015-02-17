from .atom import Atom
from .lists import SExpression as S, NIL
from .constants import undefined, T, F


def atom(x):
    """atom[x] has the value of T or F according to whether x is an
    atomic symbol.

    Thus
        atom [X] = T
        atom [(X · A)] = F

    section 3c, page 10
    """
    return T if isinstance(x, Atom) else F


def eq(x, y):
    if atom(x) is T and atom(y) is T:
        return T if repr(x) == repr(y) else F
    else:
        return undefined


def car(x):
    if atom(x) is F:
        return x.first
    else:
        return undefined


def cdr(x):
    assert atom(x) is F
    return x.second


def cons(x, y):
    return S(x, y)


def ff(x):
    if atom(x) is T:
        return x
    else:
        return ff(car(x))


def subst(x, y, z):
    """return z with all y replaced with x"""
    if atom(z) is T:
        if eq(z, y) is T:
            return x
        else:
            return z
    else:
        return S(
            subst(x, y, car(z)),
            subst(x, y, cdr(z)),
        )


def equal(x, y):
    return (
        atom(x) and
        atom(y) and
        eq(x, y)
    ) or (
        not atom(x) and
        not atom(y) and
        equal(car(x), car(y)) and
        equal(cdr(x), cdr(y))
    )


def null(x):
    return atom(x) and eq(x, NIL)


def subst2(x, y, z):
    if atom(z) is T:
        if eq(y, z) is T:
            return x
        else:
            return z
    else:
        return S(
            subst2(x, y, car(z)),
            subst2(x, z, cdr(z)),
        )


def caar(x):
    return car(car(x))


def cadar(x):
    return car(cdr(car(x)))


def append(x, y):
    if null(x) is T:
        return y
    else:
        cons(car(x), append(cdr(x), y))

# TODO: assert example


def among(x, y):
    return not null(y) and (
        equal(x, car(y)) or
        among(x, cdr(y))
    )


def pair(x, y):
    if null(x) is T and null(y) is T:
        return NIL
    elif atom(x) is F and atom(y) is F:
        return cons(
            cons(car(x), car(y)),
            pair(cdr(x), cdr(y)),
        )

# TODO: assert example


def assoc(x, y):
    if eq(caar(y), x) is T:
        return cadar(y)
    else:
        return assoc(x, cdr(y))

# TODO: assert example


def sub2(x, z):
    if null(x) is T:
        return z
    elif eq(caar(x), z) is T:
        return cadar(x)
    else:
        return sub2(cdr(x), z)


def sublis(x, y):
    if atom(y) is T:
        return sub2(x, y)
    else:
        return cons(
            sublis(x, car(y)),
            sublis(x, cdr(y)),
        )
