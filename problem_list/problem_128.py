from typing import List


def longest_consecutive(nums: List[int]) -> int:
    hash_table = set(nums)
    longest_seq = 0
    nums_checked = set()

    for num in nums:
        previous = num - 1
        if num not in nums_checked and previous not in hash_table:
            seq_length = 1
            while num + seq_length in hash_table:
                seq_length += 1
            longest_seq = max(longest_seq, seq_length)
            nums_checked.add(num)
    return longest_seq
