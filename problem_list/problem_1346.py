def check_if_exist(arr: list[int]) -> bool:
    passed = set()
    for num in arr:
        if num * 2 in passed:
            return True
        elif num % 2 == 0 and num / 2 in passed:
            return True
        if num not in passed:
            passed.add(num)
    return False


# arr = [10, 2, 5, 3]
# Output: true
# Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

arr = [3, 1, 7, 11]
# Output: false
# Explanation: There is no i and j that satisfy the conditions.

print(check_if_exist(arr))
