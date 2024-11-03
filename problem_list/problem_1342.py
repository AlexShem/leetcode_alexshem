def number_of_steps(num: int) -> int:
    count = 0
    while num > 0:
        if num % 2 == 0:
            num >>= 1
        else:
            num -= 1
        count += 1
        
    return count


if __name__ == "__main__":
    # Test Case 1
    n = 14
    expected_output = 6
    result = number_of_steps(n)
    print(f"Input: num = {n}")
    print(f"Output: {result}")
    print(f"Expected: {expected_output}")
    print(f"Test Passed: {result == expected_output}\n")

    # Test Case 2
    n = 8
    expected_output = 4
    result = number_of_steps(n)
    print(f"Input: num = {n}")
    print(f"Output: {result}")
    print(f"Expected: {expected_output}")
    print(f"Test Passed: {result == expected_output}\n")

    # Test Case 3
    n = 123
    expected_output = 12
    result = number_of_steps(n)
    print(f"Input: num = {n}")
    print(f"Output: {result}")
    print(f"Expected: {expected_output}")
    print(f"Test Passed: {result == expected_output}\n")
