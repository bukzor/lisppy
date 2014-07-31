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
        if self.second is NIL:
            return
        for x in self.second:
            yield x
S = SExpression

class NIL(SExpression):
    def __init__(self):
        self.first = self
        self.second = self
    def __repr__(self):
        return 'NIL'
NIL = NIL()  # singleton.

print '%r == %r' % ([1, 2, 3], S(1, S(2, S(3, NIL))))
assert [1, 2, 3] == list(S(1, S(2, S(3, NIL))))
print 'True\n'

# [1, 2, 3] == (1 · (2 · (3 · NIL)))
# True
