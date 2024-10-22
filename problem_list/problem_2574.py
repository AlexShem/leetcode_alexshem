from typing import List


def left_right_difference(nums: List[int]) -> List[int]:
    len_nums = len(nums)
    left_sum = [0] * len_nums
    right_sum = [0] * len_nums
    
    for i in range(1, len_nums):
        left_sum[i] += left_sum[i - 1] + nums[i - 1]
        right_sum[-i - 1] += right_sum[-i] + nums[-i]

    out = [abs(left_sum[i] - right_sum[i]) for i in range(len_nums)]

    return out
