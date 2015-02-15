from .lists import SExpression as S, NIL
from .constants import undefined


def atom(x):
    return not isinstance(x, S)


def eq(x, y):
    if atom(x) and atom(y):
        return repr(x) == repr(y)
    else:
        return undefined


def car(x):
    if not atom(x):
        return x.first
    else:
        return undefined


def cdr(x):
    assert not atom(x)
    return x.second


def cons(x, y):
    return S(x, y)


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
    if atom(z):
        if eq(y, z):
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
    if null(x):
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
    if null(x) and null(y):
        return NIL
    elif not atom(x) and not atom(y):
        return cons(
            cons(car(x), car(y)),
            pair(cdr(x), cdr(y)),
        )

# TODO: assert example


def assoc(x, y):
    if eq(caar(y), x):
        return cadar(y)
    else:
        return assoc(x, cdr(y))

# TODO: assert example


def sub2(x, z):
    if null(x):
        return z
    elif eq(caar(x), z):
        return cadar(x)
    else:
        return sub2(cdr(x), z)


def sublis(x, y):
    if atom(y):
        return sub2(x, y)
    else:
        return cons(
            sublis(x, car(y)),
            sublis(x, cdr(y)),
        )
