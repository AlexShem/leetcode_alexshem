from problem_list.problem_1386 import max_number_of_families

tests = [
    {'input': {"n": 3, "reserved_seats": [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]}, 'expected': 4},
    {'input': {"n": 2, "reserved_seats": [[2, 1], [1, 8], [2, 6]]}, 'expected': 2},
    {'input': {"n": 4, "reserved_seats": [[4, 3], [1, 4], [4, 6], [1, 7]]}, 'expected': 4},
]

NUMBER_OF_TESTS = len(tests)


def test(test_no: int = 1, test_set: list = None) -> bool:
    if test_set is None:
        test_set = tests
    if test_no not in range(1, len(tests) + 1):
        raise ValueError("Test number not supported")

    data = test_set[test_no - 1]

    result = max_number_of_families(data['input']['n'], data['input']['reserved_seats'])
    return result == data['expected']
