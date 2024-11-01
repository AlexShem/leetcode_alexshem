from heapq import heapify


def k_weakest_rows(mat: list[list[int]], k: int) -> list[int]:
    count = [sum(row) for row in mat]
    row_number = [i for i in range(len(count))]

    row_number.sort(key=lambda x: count[x])
    return row_number[:k]


# Input
mat = [[1, 1, 0, 0, 0],
       [1, 1, 1, 1, 0],
       [1, 0, 0, 0, 0],
       [1, 1, 0, 0, 0],
       [1, 1, 1, 1, 1]]

k = 3
# Output: [2, 0, 3]
print(k_weakest_rows(mat, k))
