from heapq import heapify, heappop, heappush
from random import randint, choices
from typing import List


def find_kth_largest(nums: List[int], k: int) -> int:
    heap = nums[:k]
    heapify(heap)

    for value in nums[k:]:
        if value > heap[0]:
            heappop(heap)
            heappush(heap, value)

    return heappop(heap)


print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))

print(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))

nums_length = randint(1, 10_000)
kth = 20
numbers = choices(range(-10_000, 10_000), k=nums_length)

kth_largest = find_kth_largest(numbers, kth)
print(kth_largest)
