from problem_list.problem_804 import unique_morse_representations

tests = [
    {'input': ["gin", "zen", "gig", "msg"], 'expected': 2},
    {'input': ["a"], 'expected': 1},
]

NUMBER_OF_TESTS = len(tests)


def test(test_no: int = 1, test_set: list = None) -> bool:
    if test_set is None:
        test_set = tests
    if test_no not in range(1, len(tests) + 1):
        raise ValueError("Test number not supported")

    data = test_set[test_no - 1]

    result = unique_morse_representations(data['input'])
    return result == data['expected']
