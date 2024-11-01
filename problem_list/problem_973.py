import heapq


def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    heap = []
    for point in points:
        dist = point[0] * point[0] + point[1] * point[1]
        if len(heap) == k:
            heapq.heappushpop(heap, (-dist, point))
        else:
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
