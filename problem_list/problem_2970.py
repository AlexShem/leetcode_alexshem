def incremovable_subarray_count(nums: list[int]) -> int:
    n = len(nums)
    res = 0
    for i in range(n):
        for j in range(i, n):
            subarray = nums[0:i] + nums[j + 1:n]
            if all(x < y for x, y in zip(subarray, subarray[1:])):
                res += 1
    return res
