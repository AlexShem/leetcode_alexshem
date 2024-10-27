def pivot_index(nums: list[int]) -> int:
    n = len(nums)
    left_sum = 0
    right_sum = sum(nums) - nums[0]

    if right_sum == 0:
        return 0

    for i in range(1, n):
        left_sum += nums[i - 1]
        right_sum -= nums[i]
        if left_sum == right_sum:
            return i

    return -1
