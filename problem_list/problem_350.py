from collections import Counter


def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    counter_1 = Counter(nums1)
    counter_2 = Counter(nums2)
    common = counter_1 & counter_2
    tmp = [[k] * v for k, v in common.items()]
    result = [v for row in tmp for v in row]
    return result


if __name__ == "__main__":
    # Test 1
    numbers_1 = [1, 2, 2, 1]
    numbers_2 = [2, 2]
    print(intersect(numbers_1, numbers_2))

    # Test 2
    numbers_1 = [4, 9, 5]
    numbers_2 = [9, 4, 9, 8, 4]
    print(intersect(numbers_1, numbers_2))
