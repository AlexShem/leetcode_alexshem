from typing import List
from collections import Counter


def merge_similar_items(items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
    counter_1 = Counter()
    counter_2 = Counter()

    for item in items1:
        counter_1[item[0]] += item[1]
    for item in items2:
        counter_2[item[0]] += item[1]
    out = [[k, v] for k, v in sorted((counter_1 + counter_2).items())]
    return out
