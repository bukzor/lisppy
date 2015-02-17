# coding:UTF-8
from .constants import NIL


class SExpression(object):
    """S-expressions are then defined as follows:

        1. Atomic symbols are S-expressions.
        2. If e1 and e2 are S-expressions, so is (e1 · e2).

    Examples of S-expressions are

        AB
        (A · B)
        ((AB · C) · D)

    An S-expression is then simply an ordered pair, the terms of which may be
    atomic symbols or simpler S-expressions.  We can can represent a list of
    arbitrary length in terms of S-expressions as follows. The list

        (m1, m2, · · · , mn)

    is represented by the S-expression

        (m1 · (m2 · (· · ·(mn · NIL)· · ·)))

    Here NIL is an atomic symbol used to terminate lists


    section 3a, page 8
    """
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __repr__(self):
        return u'(%s · %s)' % (self.first, self.second)

    def __iter__(self):
        yield self.first
        if self.second is NIL:
            return
        for x in self.second:
            yield x

    def __eq__(self, other):
        if isinstance(other, SExpression):
            return (
                self.first == other.first and
                self.second == other.second
            )
        else:
            return NotImplemented

    def __ne__(self, other):
        return not self == other

    @property
    def abbreviation(self):
        """Since many of the symbolic expressions with which we deal are
        conveniently expressed as lists, we shall introduce a list notation to
        abbreviate certain S-expressions.

        We have

          1. (m) stands for (m ·NIL).
          2. (m1, · · · , mn) stands for (m1 · (· · ·(mn · NIL)· · ·)).
          3. (m1, · · · , mn · x) stands for (m1 · (· · ·(mn · x)· · ·)).

        Subexpressions can be similarly abbreviated. Some examples of these
        abbreviations are

            ((AB, C), D) for ((AB · (C · NIL)) · (D · NIL))
            ((A, B), C, D · E) for ((A · (B · NIL)) · (C · (D · E)))

        section 3a, page 9
        """
        # we only abbreviate if second is NIL or S
        if self.second is NIL:
            return [self.first]
        elif isinstance(self.second, S):
            second = self.second.abbreviation
            if isinstance(second, list):
                return [self.first] + second
            else:
                return [self.first, second]
        else:
            return self


S = SExpression  # pylint:disable=invalid-name
