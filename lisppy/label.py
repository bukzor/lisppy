# demo of the label function
# TODO: make it work, test it.


def label(label, fn):
    del label, fn


def factorial(n):
    del n


label(
    'factorial',
    lambda n: 1 if n == 0 else n * factorial(n - 1)
)
