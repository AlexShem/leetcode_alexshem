import heapq
import math


def distance(point_1: list[int], point_2=None) -> float:
    if point_2 is None:
        point_2 = [0, 0]
    return math.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)


def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    heap = []
    for point in points:
        dist = distance(point)
        if len(heap) < k:
            heapq.heappush(heap, (-dist, point))
        elif -dist > heap[0][0]:
            heapq.heappop(heap)
            heapq.heappush(heap, (-dist, point))

    return [closest_points for _, closest_points in heap]


points = [[1, 3], [-2, 2]]
k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

# points = [[1, 3], [-2, 2], [1, 1]]
# k = 2

print(k_closest(points, k))
