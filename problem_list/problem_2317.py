from functools import reduce


def maximum_xor(nums: list[int]) -> int:
    nums_xor = reduce(lambda x, y: x ^ y, nums)


if __name__ == '__main__':
    nums = [3, 2, 4, 6]
    result = maximum_xor(nums)  # Expected Output: 7
    print(result)

    nums = [1, 2, 3, 9, 2]
    result = maximum_xor(nums)  # Expected Output: 11
    print(result)
