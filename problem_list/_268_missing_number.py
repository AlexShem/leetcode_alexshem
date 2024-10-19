from typing import List


def missing_number(nums: List[int]) -> int:
    nums_len = len(nums)
    nums_set = set(nums)
    full_set = set(range(nums_len + 1))
    return full_set.difference(nums_set).pop()
