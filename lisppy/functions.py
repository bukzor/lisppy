# pylint:disable=invalid-name,missing-docstring
from .lists import SExpression, NIL


def atom(x):
    return not isinstance(SExpression, x)


def eq(x, y):
    assert atom(x)
    assert atom(y)
    return x == y


def car(x):
    assert not atom(x)
    return x.first


def cdr(x):
    assert not atom(x)
    return x.second


def cons(x, y):
    return SExpression(x, y)


def ff(x):
    if atom(x):
        return x
    else:
        return ff(car(x))


def subst(x, y, z):
    """return z with all y replaced with x"""
    if atom(z):
        if eq(z, y):
            return x
        else:
            return z
    else:
        return SExpression(
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
    if atom(z):
        if eq(y, z):
            return x
        else:
            return z
    else:
        return SExpression(
            subst2(x, y, car(z)),
            subst2(x, z, cdr(z)),
        )
