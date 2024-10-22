from problem_list.problem_2574 import left_right_difference

NUMBER_OF_TESTS = 2


def test(test_no: int = 1) -> bool:
    if test_no not in range(1, NUMBER_OF_TESTS):
        raise ValueError("Test number not supported")
    if test_no == 1:
        nums = [10, 4, 8, 3]
        expected = [15, 1, 11, 22]
    if test_no == 2:
        nums = [1]
        expected = [0]

    result = left_right_difference(nums)
    return result == expected
