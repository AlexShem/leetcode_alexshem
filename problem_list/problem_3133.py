def min_end(n: int, x: int) -> int:
    n_zeros = x.bit_length() - x.bit_count()
    filler = n - 1
    new_val = bin(x)[2:]
    if filler > n_zeros:
        new_val = new_val.rjust(len(new_val) + filler - n_zeros, '0')
    i = len(new_val) - 1
    filler = bin(filler)[2:]
    while i >= 0 and len(filler) > 0:
        if new_val[i] == '0':
            new_val = new_val[0:i] + filler[-1] + new_val[(i + 1):]
            filler = filler[:-1]
        i -= 1
    new_val = int(new_val, 2)
    return new_val


if __name__ == '__main__':
    n = 3
    x = 4
    # result = min_end(n, x)  # Expected Output: 6
    # print(result)

    n = 2
    x = 7
    # result = min_end(n, x)  # Expected Output: 15
    # print(result)

    n = 3
    x = 10
    # result = min_end(n, x)  # Expected Output: 14
    # print(result)

    n = 39_631_251
    x = 47_324_986
    result = min_end(n, x)  # Expected Output: ?
    print(result)
