def valid_anagram(s: str, t: str) -> bool:
    val = sorted(s) == sorted(t)
    return val
