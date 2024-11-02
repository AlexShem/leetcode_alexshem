def maximum_even_split(final_sum: int) -> list[int]:
    """Splits the given `final_sum` into a sum of the maximum number of unique positive even integers.

    :param final_sum: (int): The integer to be split.

    :returns: list[int]: A list of unique positive even integers that sum up to `final_sum`.
               Returns an empty list if no valid split exists.
    """

    if final_sum % 2 == 1:
        return []

    split = []
    split_sum = 0
    term = 2
    # Apply greedy search starting from 2
    while True:
        split.append(term)
        split_sum += term

        if split_sum == final_sum:
            return split
        elif split_sum < final_sum:
            term += 2
        elif split_sum > final_sum:
            split_sum -= term
            term = final_sum - split_sum
            del split[-1]

            while len(split) and term in split:
                split_sum -= split[-1]
                del split[-1]
                term = final_sum - split_sum


if __name__ == "__main__":
    # Test Case 1
    final_sum_input = 12
    expected_output = [2, 4, 6]
    result = maximum_even_split(final_sum_input)
    print(f"Input: finalSum = {final_sum_input}")
    print(f"Output: {result}")
    print(f"Expected: {expected_output}")
    print(f"Test Passed: {sorted(result) == sorted(expected_output)}\n")

    # Test Case 2
    final_sum_input = 7
    expected_output = []
    result = maximum_even_split(final_sum_input)
    print(f"Input: finalSum = {final_sum_input}")
    print(f"Output: {result}")
    print(f"Expected: {expected_output}")
    print(f"Test Passed: {result == expected_output}\n")

    # Test Case 3
    final_sum_input = 28
    expected_output = [2, 4, 6, 16]  # Note: The expected output can vary as long as the sum is correct
    result = maximum_even_split(final_sum_input)
    print(f"Input: finalSum = {final_sum_input}")
    print(f"Output: {result}")
    print(f"Expected: {expected_output}")
    # Since the problem allows any order, sort both lists before comparison
    print(f"Test Passed: {sum(result) == final_sum_input and len(result) == len(expected_output)}\n")

    # Additional Test Cases can be added below following the same structure

    # Test Case 4
    final_sum_input = 950
    expected_output = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50,
                       52, 54, 56, 58, 80]
    result = maximum_even_split(final_sum_input)
    print(f"Input: finalSum = {final_sum_input}")
    print(f"Output: {result}")
    print(f"Expected: {expected_output}")
    # Since the problem allows any order, sort both lists before comparison
    print(f"Test Passed: {sum(result) == final_sum_input and len(result) == len(expected_output)}\n")
