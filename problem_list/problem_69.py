from math import floor


def my_sqrt(x: int) -> int:
    def newton_step(a: int, x0: float = 10) -> float:
        # Function: f(x) = x**2 - a
        # f(x) = f(x0) + f'(x) (x - x0) = 0
        # ==> x = -f(x0)/f'(x0) + x0
        return x0 - (x0 ** 2 - a) / (2 * x0)

    if x in [0, 1]:
        return 0

    tolerance = 1E-2
    init_val = x / 2
    root = newton_step(x, init_val)

    while abs(root - init_val) > tolerance:
        init_val = root
        root = newton_step(x, init_val)

    return floor(root)


# print(my_sqrt(4))
# print(my_sqrt(8))
# print(my_sqrt(105))
print(my_sqrt(8192))
