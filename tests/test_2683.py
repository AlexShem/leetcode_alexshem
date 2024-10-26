from problem_list.problem_2683 import does_valid_array_exist

tests = [
    {'input': [1, 1, 0], 'expected': True},
    {'input': [1, 1], 'expected': True},
    {'input': [1, 0], 'expected': False},
    {'input': [0, 1, 1, 0, 0], 'expected': True}
]

NUMBER_OF_TESTS = len(tests)


def test(test_no: int = 1, test_set: list = None) -> bool:
    if test_set is None:
        test_set = tests
    if test_no not in range(1, len(tests) + 1):
        raise ValueError("Test number not supported")

    data = test_set[test_no - 1]
    
    result = does_valid_array_exist(data['input'])
    return result == data['expected']
