from typing import List
from collections import Counter


def merge_similar_items(items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
    cntr = Counter()

    for k, v in items1 + items2:
        cntr[k] += v

    return [list(item) for item in sorted(cntr.items())]
