from string import ascii_lowercase


def kth_character(k: int) -> str:
    word = 'a'
    while len(word) < k:
        expanded = word
        for char in expanded:
            word += chr((ord(char) + 1 - ord('a')) % 26 + ord('a'))
    return word[k - 1]


k = 5
# Output: "b"
# Explanation:
# Initially, word = "a". We need to do the operation three times:
# Generated string is "b", word becomes "ab".
# Generated string is "bc", word becomes "abbc".
# Generated string is "bccd", word becomes "abbcbccd".

k = 10
# Output: "c"

print(kth_character(k))
