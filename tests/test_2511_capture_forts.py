from problem_list._2511_capture_forts import capture_forts

NUMBER_OF_TESTS = 3


def test(test_no: int = 1) -> bool:
    if test_no not in range(1, NUMBER_OF_TESTS):
        raise ValueError("Test number not supported")
    if test_no == 1:
        forts = [1, 0, 0, -1, 0, 0, 0, 0, 1]
        expected = 4
    if test_no == 2:
        forts = [0, 0, 1, -1]
        expected = 0
    if test_no == 3:
        forts = [-1, 0, 1, 0, -1, 1]
        expected = 1

    result = capture_forts(forts)
    return result == expected
