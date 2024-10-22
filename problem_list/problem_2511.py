from itertools import groupby
from typing import List


def capture_forts(forts: List[int]) -> int:
    grp = [(k, len(list(g))) for k, g in groupby(forts)]
    out = 0

    for i in range(1, len(grp) - 1):
        if grp[i - 1][0] * grp[i + 1][0] == -1:
            out = max(out, grp[i][1])
    return out
