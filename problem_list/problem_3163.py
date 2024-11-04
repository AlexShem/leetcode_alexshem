def compressed_string(word: str) -> str:
    comp = ""
    count = 1
    buffer = word[0]
    for char in word[1:]:
        if char == buffer and count < 9:
            count += 1
        else:
            comp += f"{count}{buffer}"
            count = 1
            buffer = char

    comp += f"{count}{buffer}"
    return comp


if __name__ == "__main__":
    word = "abcde"
    result = compressed_string(word)  # Expected output: "1a1b1c1d1e"
    print(result)

    word = "aaaaaaaaaaaaaabb"
    result = compressed_string(word)  # Expected output: "9a5a2b"
    print(result)
