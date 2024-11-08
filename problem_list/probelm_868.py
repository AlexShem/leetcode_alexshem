def binary_gap(n: int) -> int:
    n_binary = bin(n)[2:]
    left = 0
    right = 0
    distance = 0

    for i in range(1, len(n_binary)):
        if n_binary[i] == '1':
            right = i
            distance = max(distance, right - left)
            left = i

    return distance


if __name__ == '__main__':
    n = 22
    result = binary_gap(n)  # Expected Output: 2
    print(result)

    n = 8
    result = binary_gap(n)  # Expected Output: 0
    print(result)

    n = 5
    result = binary_gap(n)  # Expected Output: 2
    print(result)
