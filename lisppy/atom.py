from .misc import getstate


class Atom(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __getstate__(self):
        return self.name

    def __eq__(self, other):
        return isinstance(other, Atom) and getstate(self) == getstate(other)

    def __ne__(self, other):
        return not self == other
