from bisect import bisect_right


def next_greatest_letter(letters: list[str], target: str) -> str:
    idx = bisect_right(letters, target)
    return letters[idx] if idx < len(letters) else letters[0]


# letters = ["c", "f", "j"]
# target = "a"
# Output: "c"

# letters = ["c", "f", "j"]
# target = "c"
# Output: "f"

letters = ["x", "x", "y", "y"]
target = "z"
# Output: "x"

print(next_greatest_letter(letters, target))
