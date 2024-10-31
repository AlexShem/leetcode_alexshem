def special_array(nums: list[int]) -> int:
    nums.sort(reverse=True)
    left = 0
    right = len(nums)

    while left != right:
        mid = (left + right) // 2
        if nums[mid] >= mid:
            left = mid + 1
        else:
            right = mid - 1

    if left == 0:
        return -1
    elif left == len(nums):
        return left if nums[-1] > left else -1
    elif nums[left] < left:
        return left
    else:
        return -1


# nums = [4, 4, 3, 0, 0]
# nums = [3, 5]
# nums = [0, 0]
# nums = [3, 6, 7, 7, 0]
nums = [3, 9, 7, 8, 3, 8, 6, 6]  # Expected: 6
print(special_array(nums))
