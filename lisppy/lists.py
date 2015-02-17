# coding:UTF-8
from .constants import NIL


class SExpression(object):
    "section 3.a, page 8"
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

S = SExpression  # pylint:disable=invalid-name
