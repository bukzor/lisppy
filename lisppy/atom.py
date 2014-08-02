class Atom(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name
    def __eq__(self, other):
        return (repr(self) == repr(other))
    def __ne__(self, other):
        return not (self == other)

NIL = Atom('NIL')