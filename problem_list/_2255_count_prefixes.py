from typing import List


def count_prefixes(words: List[str], s: str) -> int:
    out = 0
    for word in words:
        if s.startswith(word):
            out += 1
    return out
