def find_gcd(nums: list[int]) -> int:
    def gcd(a: int, b: int) -> int:
        while b != 0:
            t = a % b
            a = b
            b = t
        return a

    return gcd(max(nums), min(nums))


if __name__ == "__main__":
    # numbers = [2, 5, 6, 9, 10]
    numbers = [7, 5, 6, 8, 3]
    print(find_gcd(numbers))
