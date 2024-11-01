def is_perfect_square(num: int) -> bool:
    left = 1
    right = num

    while left <= right:
        mid = (left + right) // 2
        if mid * mid == num:
            return True
        elif mid * mid < num:
            left = mid + 1
        else:
            right = mid - 1
    return False


num = 16
# Output: true
# Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

# num = 14
# Output: false
# Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.

num = 2_147_483_647

print(is_perfect_square(num))
