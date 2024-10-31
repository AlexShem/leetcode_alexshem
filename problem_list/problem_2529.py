def maximum_count(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1

    if nums[left] == 0 and nums[right] == 0:
        return 0
    elif nums[left] * nums[right] > 0:
        return right + 1

    while right - left > 1:
        middle = (left + right) // 2
        if nums[middle] == 0:
            middle_left, middle_right = middle - 1, middle + 1
            while middle_left > 0 and nums[middle_left] == 0:
                middle_left -= 1
            while middle_right < len(nums) - 1 and nums[middle_right] == 0:
                middle_right += 1
            return max(middle_left + 1, len(nums) - middle_right)
        else:
            if nums[middle] < 0:
                left = middle
            else:
                right = middle
    return max(left + 1, len(nums) - right)


# ins = [-3, -2, -1, 0, 0, 1, 2]
# ins = [-2, -1, -1, 1, 2, 3]
# ins = [5, 20, 66, 1314]
ins = [-2, -1, -1, 0, 0, 0]
print(maximum_count(ins))
