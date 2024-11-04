import heapq

def delete_greatest_value(grid: list[list[int]]) -> int:
    grid = [[-element for element in row] for row in grid]

    for row in grid:
        heapq.heapify(row)

    res = 0
    for _ in range(len(grid[0])):
        max_vals = [-heapq.heappop(grid[i]) for i in range(len(grid))]
        res += max(max_vals)
    return res


if __name__ == "__main__":
    matrix = [[1, 2, 4], [3, 3, 1]]
    result = delete_greatest_value(matrix) # Expected output: 8
    print(result)

    matrix = [[10]]
    result = delete_greatest_value(matrix) # Expected output: 10
    print(result)

    matrix = [[35,52,74,92,25],[65,77,1,73,32],[43,68,8,100,84],[80,14,88,42,53],[98,69,64,40,60]]
    result = delete_greatest_value(matrix)  # Expected output: 352
    print(result)