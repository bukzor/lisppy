from .sexpression import SExpression


class Atom(SExpression):
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

    ...  Atomic symbols are S-expressions.

    section 3a1, page 8
    """
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __getstate__(self):
        return self.name
