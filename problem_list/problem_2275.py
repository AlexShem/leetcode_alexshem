def largest_combination(candidates: list[int]) -> int:
    binary = [bin(num)[2:] for num in candidates]
    longest_binary = max(map(len, binary))
    binary = [element.rjust(longest_binary, '0') for element in binary]

    max_bites = [0] * longest_binary
    for i in range(longest_binary):
        max_bites[i] = sum([int(element[i]) for element in binary])

    max_number = max(max_bites)
    return max_number


if __name__ == '__main__':
    # Test 1
    candidates = [16, 17, 71, 62, 12, 24, 14]
    result = largest_combination(candidates)  # Expected output: 4
    print(result)

    # Test 2
    candidates = [8, 8]
    result = largest_combination(candidates)  # Expected output: 2
    print(result)
