fib_values = {0: 0, 1: 1}


def fib(n: int) -> int:
    if n in fib_values:
        return fib_values[n]

    fib_values[n] = fib(n - 2) + fib(n - 1)
    return fib_values[n]
