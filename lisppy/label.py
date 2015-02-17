# demo of the label function
# TODO: make it work, test it.
# flake8: noqa, pylint: skip-file

label(
    'factorial',
    lambda n: 1 if n == 0 else n * factorial(n - 1)
)
