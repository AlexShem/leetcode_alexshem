from problem_list.problem_2529 import maximum_count

tests = [
    {'input': [-2, -1, -1, 1, 2, 3], 'expected': 3},
    {'input': [-3, -2, -1, 0, 0, 1, 2], 'expected': 3},
    {'input': [5, 20, 66, 1314], 'expected': 4},
    {'input': [-2, -1, -1, 0, 0, 0], 'expected': 3},
]

NUMBER_OF_TESTS = len(tests)


def test(test_no: int = 1, test_set: list = None) -> bool:
    if test_set is None:
        test_set = tests
    if test_no not in range(1, len(tests) + 1):
        raise ValueError("Test number not supported")

    data = test_set[test_no - 1]

    result = maximum_count(data['input'])
    return result == data['expected']
