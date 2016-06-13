# coding:UTF-8
from .constants import NIL
from .sexpression import SExpression


class Pair(SExpression):
    """If e1 and e2 are S-expressions, so is (e1 · e2).

    section 3a, page 8
    """
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __repr__(self):
        return '(%s · %s)' % (abbrev.first, abbrev.second)

    def __str__(self):
        return repr(self.abbreviation)

    def __iter__(self):
        yield self.first
        if self.second is NIL:
            return
        elif isinstance(self.second, Pair):
            for x in self.second:
                yield x
        else:
            yield self.second

    def __getstate__(self):
        return tuple(self)

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
        if isinstance(self.first, Pair):
            first = self.first.abbreviation
        else:
            first = self.first

        if isinstance(self.second, Pair):
            second = self.second.abbreviation
        elif self.second is NIL:
            second = []
        else:
            second = self.second

        if isinstance(second, list):
            return [first] + second
        else:
            return Pair(first, second)
