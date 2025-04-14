def min_end(n: int, x: int) -> int:
    zero_bits = x ^ (2 ** x.bit_length() - 1)
    bits_to_change = n - 1
    return zero_bits


if __name__ == '__main__':
    n = 3
    x = 4
    result = min_end(n, x)  # Expected Output: 6
    print(result)

    n = 2
    x = 7
    result = min_end(n, x)  # Expected Output: 15
    print(result)

    n = 3
    x = 10
    result = min_end(n, x)  # Expected Output: 14
    print(result)

    n = 39_631_251
    x = 47_324_986
    result = min_end(n, x)  # Expected Output: ?
    print(result)
