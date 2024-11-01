from bisect import bisect_right


def answer_queries(nums: list[int], queries: list[int]) -> list[int]:
    nums.sort()
    answer = [0] * len(queries)
    cum_sums = [0] * len(nums)
    cum_sums[0] = nums[0]
    for i in range(1, len(nums)):
        cum_sums[i] = cum_sums[i - 1] + nums[i]

    for i, q in enumerate(queries):
        idx = bisect_right(cum_sums, q)
        answer[i] = idx

    return answer


# nums = [4, 5, 2, 1]
# queries = [3, 10, 21]
# Output: [2,3,4]
# Explanation: We answer the queries as follows:
# - The subsequence [2,1] has a sum less than or equal to 3. It can be proven that 2 is the maximum size of such a subsequence, so answer[0] = 2.
# - The subsequence [4,5,1] has a sum less than or equal to 10. It can be proven that 3 is the maximum size of such a subsequence, so answer[1] = 3.
# - The subsequence [4,5,2,1] has a sum less than or equal to 21. It can be proven that 4 is the maximum size of such a subsequence, so answer[2] = 4.

nums = [2, 3, 4, 5]
queries = [1]
# Output: [0]
# Explanation: The empty subsequence is the only subsequence that has a sum less than or equal to 1, so answer[0] = 0.

print(answer_queries(nums, queries))
