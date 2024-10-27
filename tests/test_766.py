from problem_list.problem_766 import is_toeplitz_matrix

tests = [
    {'input': [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]], 'expected': True},
    {'input': [[1, 2], [2, 2]], 'expected': False},
]

NUMBER_OF_TESTS = len(tests)


def test(test_no: int = 1, test_set: list = None) -> bool:
    if test_set is None:
        test_set = tests
    if test_no not in range(1, len(tests) + 1):
        raise ValueError("Test number not supported")

    data = test_set[test_no - 1]

    result = is_toeplitz_matrix(data['input'])
    return result == data['expected']
