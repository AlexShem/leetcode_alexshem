from typing import List


def missing_number(nums: List[int]) -> int:
    n = len(nums)
    total_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return total_sum - actual_sum
