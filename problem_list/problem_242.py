from collections import Counter

def valid_anagram(s: str, t: str) -> bool:
    s_letter_count = Counter(s)
    s_letter_count.subtract(Counter(t))
    
    for value in s_letter_count.values():
        if value != 0:
            return False
    
    return True
