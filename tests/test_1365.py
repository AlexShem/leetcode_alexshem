from problem_list.problem_1365 import smaller_numbers_than_current

tests = [
    {'input': [8, 1, 2, 2, 3], 'expected': [4, 0, 1, 1, 3]},
    {'input': [6, 5, 4, 8], 'expected': [2, 1, 0, 3]},
    {'input': [7, 7, 7, 7], 'expected': [0, 0, 0, 0]},
]

NUMBER_OF_TESTS = len(tests)


def test(test_no: int = 1, test_set: list = None) -> bool:
    if test_set is None:
        test_set = tests
    if test_no not in range(1, len(tests) + 1):
        raise ValueError("Test number not supported")

    data = test_set[test_no - 1]

    result = smaller_numbers_than_current(data['input'])
    return result == data['expected']
