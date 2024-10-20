from collections import deque
from typing import List


# TODO: Problem not Solved
def capture_forts(forts: List[int]) -> int:
    stack = deque()
    captures_sum = set()
    captures = 0
    for i, fort in enumerate(forts):
        if fort == -1:
            stack.append(i)
            continue
        if fort == 0:
            captures += 1
            continue
        if fort == 1:
            if len(stack):
                captures_sum.add(captures)
                captures = 0
                stack.pop()
    return max(captures_sum)
