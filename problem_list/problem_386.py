def lexical_order(n: int) -> list[int]:
    def dfs(current: int, out: list[int]) -> None:
        if current > n:
            return
        out.append(current)

        for k in range(10):
            next_value = current * 10 + k
            if next_value > n:
                return
            dfs(next_value, out)

    result: list[int] = []
    for i in range(1, 10):
        dfs(i, result)

    return result


if __name__ == "__main__":
    # Constraints: 1 <= n <= 5 * 10^4
    num = 13
    res = lexical_order(num)  # Expected Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
    print(res)
