from problem_list.problem_509 import fib

tests = [
    {'input': 2, 'expected': 1},
    {'input': 3, 'expected': 2},
    {'input': 4, 'expected': 3},
]

NUMBER_OF_TESTS = len(tests)


def test(test_no: int = 1, test_set: list = None) -> bool:
    if test_set is None:
        test_set = tests
    if test_no not in range(1, len(tests) + 1):
        raise ValueError("Test number not supported")

    data = test_set[test_no - 1]

    result = fib(data['input'])
    return result == data['expected']
