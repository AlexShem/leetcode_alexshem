from itertools import groupby


def make_fancy_string(s: str) -> str:
    s_grouped = [list(g) for k, g in groupby(s)]

    out = ''
    for group in s_grouped:
        out += ''.join(group[0:min(len(group), 2)])
    return out


s = "leeetcode"
# Output: "leetcode"

print(make_fancy_string(s))
