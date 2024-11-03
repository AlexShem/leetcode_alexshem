import heapq

class KthLargest:
    _k_largest = list[int]
    k = int
    nums = list[int]

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = nums.copy()
        if len(self.nums) > 0:
            heapq.heapify(nums)
            self._k_largest = heapq.nlargest(k, nums)
            heapq.heapify(self._k_largest)
        else:
            self._k_largest = []

    def add(self, val: int) -> int:
        self.nums.append(val)
        if len(self._k_largest) >= self.k:
            heapq.heappushpop(self._k_largest, val)
        else:
            heapq.heappush(self._k_largest, val)
        return self._k_largest[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

if __name__ == "__main__":
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    kthLargest.add(3) # return 4
    kthLargest.add(5) # return 5
    kthLargest.add(10) # return 5
    kthLargest.add(9) # return 8
    kthLargest.add(4) # return 8

    del kthLargest

    kthLargest = KthLargest(1, [])
    kthLargest.add(-3)
    kthLargest.add(-2)
    kthLargest.add(-4)
    kthLargest.add(0)
    kthLargest.add(4)