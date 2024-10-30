def smaller_numbers_than_current(nums: list[int]) -> list[int]:
    result = [0] * len(nums)

    for i, num in enumerate(nums):
        lower = [n for n in nums if n < num]
        result[i] = len(lower)

    return result
