from problem_list._268_missing_number import missing_number

NUMBER_OF_TESTS = 3

def test(test_no: int = 1) -> bool:
    if test_no not in [1, 2, 3]:
        raise ValueError("Test number not supported")
    if test_no == 1:
        nums = [3, 0, 1]
        expected = 2
    if test_no == 2:
        nums = [0, 1]
        expected = 2
    if test_no == 3:
        nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
        expected = 8
    
    result = missing_number(nums)
    return result == expected
