# coding:UTF-8
from .atom import NIL

class SExpression(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def __repr__(self):
        return unicode(self).encode('UTF-8')
    def __unicode__(self):
        return u'(%s %s)' % (self.first, self.second)
        ## pytest can't handle utf-8 repr -.-
        #return u'(%s · %s)' % (self.first, self.second)
    def __iter__(self):
        return self._iter()
    def _iter(self):
        yield self.first
        if self.second is NIL:
            return
        for x in self.second:
            yield x
    def __eq__(self, other):
        if not isinstance(other, SExpression):
            return False
        return (
            self.first == other.first and
            self.second == other.second
        )
    def __ne__(self, other):
        return not (self == other)
S = SExpression

assert [1, 2, 3] == list(S(1, S(2, S(3, NIL)))), '%r == %r' % ([1, 2, 3], S(1, S(2, S(3, NIL))))
