from .atom import Atom
from .pair import Pair, NIL
from .constants import undefined, T, F


def atom(x):
    """atom[x] has the value of T or F according to whether x is an
    atomic symbol.

    Thus
        atom [X] = T
        atom [(X · A)] = F

    section 3c1, page 10
    """
    return T if isinstance(x, Atom) else F


def eq(x, y):
    """eq [x;y] is defined if and only if both x and y are atomic. eq [x; y]
    = T if x and y are the same symbol, and eq [x; y] = F otherwise. Thus

        eq [X; X] = T
        eq [X; A] = F
        eq [X; (X · A)] is undefined.

    section 3c2, page 10
    """
    if atom(x) is atom(y) is T:
        return T if x == y else F
    else:
        return undefined


def car(x):
    """car[x] is defined if and only if x is not atomic.
    Thus car [X] is undefined.

        car [(X · A)] = X
        car [((X · A) · Y )] = (X · A)

    section 3c3, page 11
    """
    if atom(x) is F:
        return x.first
    else:
        return undefined


def cdr(x):
    """cdr [x] is also defined when x is not atomic.
    Thus cdr [X] is undefined.

        cdr [(X · A)] = A
        cdr [((X · A) · Y )] = Y

    section 3c4, page 11
    """
    if atom(x) is F:
        return x.second
    else:
        return undefined


def cons(x, y):
    """cons [x; y] is defined for any x and y.

        cons [X; A] = (X A)
        cons [(X · A); Y ] = ((X · A)Y )

    section 3c5, page 11
    """
    return Pair(x, y)


def ff(x):
    """The value of ff[x] is the first atomic symbol of the S-expression x with
    the parentheses ignored. Thus

        ff[((A · B) · C)] = A

    section 3d1, page 12
    """
    if atom(x) is T:
        return x
    else:
        return ff(car(x))


def subst(x, y, z):
    """This function gives the result of substituting the S-expression
    x for all occurrences of the atomic symbol y in the S-expression z.

    As an example, we have

        subst[(X · A); B; ((A · B) · C)] = ((A · (X · A)) · C)

    section 3d2, page 13
    """
    if atom(z) is T:
        if eq(z, y) is T:
            return x
        else:
            return z
    else:
        return cons(
            subst(x, y, car(z)),
            subst(x, y, cdr(z)),
        )


def equal(x, y):
    """This is a predicate that has the value T if x and y are the
    same S-expression, and has the value F otherwise.

    section 3d3, page 13
    """
    return T if (
        atom(x) is
        atom(y) is
        eq(x, y) is
        T
    ) or (
        atom(x) is atom(y) is F and
        equal(car(x), car(y)) is
        equal(cdr(x), cdr(y)) is
        T
    ) else F


def null(x):
    """This predicate is useful in dealing with lists.

    section 3d3, page 13
    """

    return T if atom(x) is eq(x, NIL) is T else F


def subst2(x, y, z):
    """???"""
    if atom(z) is T:
        if eq(y, z) is T:
            return x
        else:
            return z
    else:
        return cons(
            subst2(x, y, car(z)),
            subst2(x, z, cdr(z)),
        )


def caar(x):
    """page 14"""
    return car(car(x))


def cadar(x):
    """page 14"""
    return car(cdr(car(x)))


def list_(*atoms):
    """page 14"""
    result = NIL
    for atom in reversed(atoms):
        result = cons(atom, result)  # pylint:disable=redefined-variable-type
    return result


def append(x, y):
    """section 3d1(again), page 14"""
    if null(x) is T:
        return y
    else:
        return cons(car(x), append(cdr(x), y))


def among(x, y):
    """This predicate is true if the S-expression x occurs among
    the elements of the list y.

    section 3d2(again), page 14
    """
    return null(y) is F and (
        equal(x, car(y)) is T or
        among(x, cdr(y)) is T
    )


def pair(x, y):
    """
    This function gives the list of pairs of corresponding elements of the lists x and y.
    (It's just like Python's `zip`.)

    section 3d2(again), page 14
    """
    if null(x) is null(y) is T:
        return NIL
    elif atom(x) is atom(y) is F:
        return cons(
            cons(car(x), car(y)),
            pair(cdr(x), cdr(y)),
        )
    else:
        return undefined

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
