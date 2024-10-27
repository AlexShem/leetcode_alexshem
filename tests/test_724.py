from problem_list.problem_724 import pivot_index

tests = [
    {'input': [1, 7, 3, 6, 5, 6], 'expected': 3},
    {'input': [1, 2, 3], 'expected': -1},
    {'input': [2, 1, -1], 'expected': 0},
    {'input': [-1, -1, 1, 1, 0, 0], 'expected': 4},
]

NUMBER_OF_TESTS = len(tests)


def test(test_no: int = 1, test_set: list = None) -> bool:
    if test_set is None:
        test_set = tests
    if test_no not in range(1, len(tests) + 1):
        raise ValueError("Test number not supported")

    data = test_set[test_no - 1]

    result = pivot_index(data['input'])
    return result == data['expected']
