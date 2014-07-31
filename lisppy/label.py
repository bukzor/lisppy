# demo of the label function

label('factorial',
        lambda n: 1 if n == 0 else n * factorial(n - 1)
)
