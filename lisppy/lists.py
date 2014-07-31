# coding:UTF-8

class SExpression(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def __repr__(self):
        return '(%r · %r)' % (self.first, self.second)
    def __iter__(self):
        return self._iter()
    def _iter(self):
        yield self.first
        for x in self.second:
            yield x
S = SExpression

class NIL(SExpression):
    def __init__(self, first=None, second=None):
        self.first = self
        self.second = self
    def __repr__(self):
        return 'NIL'
    def _iter(self):
        # the generator that generates nothing
        return
        yield

NIL = NIL()  # singleton.

print '%r == %r' % ([1, 2, 3], S(1, S(2, S(3, NIL))))
assert [1, 2, 3] == list(S(1, S(2, S(3, NIL))))
print 'True\n'

# [1, 2, 3] == (1 · (2 · (3 · NIL)))
# True
