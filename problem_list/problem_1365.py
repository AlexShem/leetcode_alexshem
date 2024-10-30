def smaller_numbers_than_current(nums: list[int]) -> list[int]:
    nums_sorted = sorted(nums)

    mapping = {}
    for i, num in enumerate(nums_sorted):
        if num not in mapping:
            mapping[num] = i
    
    return [mapping[num] for num in nums]
