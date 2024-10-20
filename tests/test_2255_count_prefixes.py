from problem_list._2255_count_prefixes import count_prefixes

NUMBER_OF_TESTS = 2


def test(test_no: int = 1) -> bool:
    if test_no not in range(1, NUMBER_OF_TESTS + 1):
        raise ValueError("Test number not supported")
    if test_no == 1:
        words = ["a", "b", "c", "ab", "bc", "abc"]
        s = "abc"
        expected = 3
    if test_no == 2:
        words = ["a", "a"]
        s = "aa"
        expected = 2

    result = count_prefixes(words, s)
    return result == expected
