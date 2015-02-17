from .misc import getstate


class Atom(object):
    """For atomic symbols, we shall use strings of capital Latin letters and
    digits with single imbedded blanks. (1995 remark: Imbedded blanks could be
    allowed within symbols, because lists were then written with commas between
    elements.)

    Examples of atomic symbols are

        A
        ABA
        APPLE PIE NUMBER 3

    The symbols are atomic in the sense that any substructure they may have as
    sequences of characters is ignored. We assume only that different symbols
    can be distinguished.

    section 3a, page 8
    """
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __getstate__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, Atom):
            return getstate(self) == getstate(other)
        else:
            return NotImplemented

    def __ne__(self, other):
        return not self == other
