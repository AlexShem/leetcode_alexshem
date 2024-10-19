from problem_list._242_valid_anagram import valid_anagram

NUMBER_OF_TESTS = 2

def test(test_no: int = 1) -> bool:
    if test_no not in range(1, NUMBER_OF_TESTS + 1):
        raise ValueError("Test number not supported")
    if test_no == 1:
        s = "anagram"
        t = "nagaram"
        expected = True
    elif test_no == 2:
        s = "rat"
        t = "car"
        expected = False
    
    result = valid_anagram(s, t)
    return result == expected
