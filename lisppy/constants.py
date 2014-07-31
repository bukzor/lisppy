class const(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return name

T = const('T')
F = const('F')
undefined = const('undefined')
