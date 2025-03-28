from bisect import bisect_left


def special_array(nums: list[int]) -> int:
    nums.sort()
    left = 0
    right = len(nums)

    while left <= right:
        mid = (left + right) // 2
        index = bisect_left(nums, mid)
        count = len(nums[index:])
        if count == mid:
            return mid
        elif count > mid:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# nums = [0, 0, 3, 4, 4]  # Expected: 3
# nums = [3, 5]  # Expected: 2
# nums = [0, 0]  # Expected: -1
# nums = [3, 6, 7, 7, 0]  # Expected: -1
nums = [3, 9, 7, 8, 3, 8, 6, 6]  # Expected: 6
print(special_array(nums))
