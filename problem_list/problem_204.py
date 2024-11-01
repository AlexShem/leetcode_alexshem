def count_primes(n: int) -> int:
    candidates = list(range(2, n))
    primes = [True] * len(candidates)

    for i in range(2, n // 2):
        if primes[i - 2]:
            for j in range(i ** 2, n, i):
                primes[j - 2] = False
    return sum(primes)


# n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

# n = 0
# Output: 0

# n = 1
# Output: 0

# n = 96

n = 499979

print(count_primes(n))
