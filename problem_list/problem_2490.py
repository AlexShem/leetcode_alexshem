def is_circular_sentence(sentence: str) -> bool:
    words = sentence.split(' ')
    
    if len(words) == 1:
        return words[0][0] == words[0][-1]
    
    for i in range(len(words) - 1):
        if words[i][-1] != words[i + 1][0]:
            return False
    return words[0][0] == words[-1][-1]
        

sentence = "leetcode exercises sound delightful"
# Output: true

if __name__ == "__main__":
    print(is_circular_sentence(sentence))
