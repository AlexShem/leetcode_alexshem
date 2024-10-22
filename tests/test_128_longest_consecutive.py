from problem_list._128_longest_consecutive import longest_consecutive

NUMBER_OF_TESTS = 5


def test(test_no: int = 1) -> bool:
    if test_no not in range(1, NUMBER_OF_TESTS + 1):
        raise ValueError("Test number not supported")
    if test_no == 1:
        nums = [100, 4, 200, 1, 3, 2]
        expected = 4
    if test_no == 2:
        nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        expected = 9
    if test_no == 3:
        nums = []
        expected = 0
    if test_no == 4:
        nums = [0]
        expected = 1
    if test_no == 5:
        nums = [0, 0]
        expected = 1

    result = longest_consecutive(nums)
    return result == expected
