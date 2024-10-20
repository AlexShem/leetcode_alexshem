from problem_list._2363_merge_similar_items import merge_similar_items

NUMBER_OF_TESTS = 3


def test(test_no: int = 1) -> bool:
    if test_no not in range(1, NUMBER_OF_TESTS + 1):
        raise ValueError("Test number not supported")
    if test_no == 1:
        items1 = [[1, 1], [4, 5], [3, 8]]
        items2 = [[3, 1], [1, 5]]
        expected = [[1, 6], [3, 9], [4, 5]]
    if test_no == 2:
        items1 = [[1, 1], [3, 2], [2, 3]]
        items2 = [[2, 1], [3, 2], [1, 3]]
        expected = [[1, 4], [2, 4], [3, 4]]
    if test_no == 3:
        items1 = [[1, 3], [2, 2]]
        items2 = [[7, 1], [2, 2], [1, 4]]
        expected = [[1, 7], [2, 4], [7, 1]]

    result = merge_similar_items(items1, items2)
    return result == expected
