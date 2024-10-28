from string import ascii_lowercase


def unique_morse_representations(words: list[str]) -> int:
    codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
             ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    code_map = dict(zip(ascii_lowercase, codes))

    encoded = []
    for word in words:
        encoded_word = ""
        for letter in word:
            encoded_word += code_map[letter]
        encoded.append(encoded_word)

    return len(set(encoded))
