def and_(p, q):
    # ( (p, q), (True, False) )
    if p:
        return q
    else:
        return False


def or_(p, q):
    # ( (p, True), (True, q) )
    if p:
        return True
    else:
        return q


def not_(p):
    # ( (p, False), (True, False) )
    if p:
        return False
    else:
        return True


def implies(p, q):
    if p:
        return q
    else:
        return True
