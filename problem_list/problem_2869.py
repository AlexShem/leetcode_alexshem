def min_operations(nums: list[int], k: int) -> int:
    n = len(nums)
    num_collected = [0] * k
    total_collected = 0
    i = n - 1
    while i >= 0 and not all(num_collected):
        num = nums[i]
        if num <= k and num_collected[num - 1] == 0:
            num_collected[num - 1] = 1
        total_collected += 1
        i -= 1
    return total_collected


if __name__ == '__main__':
    nums = [3, 1, 5, 4, 2]
    k = 2
    result = min_operations(nums, k)  # Expected Output: 4
    print(result)

    nums = [3, 1, 5, 4, 2]
    k = 5
    result = min_operations(nums, k)  # Expected Output: 5
    print(result)

    nums = [3, 2, 5, 3, 1]
    k = 3
    result = min_operations(nums, k)  # Expected Output: 4
    print(result)
