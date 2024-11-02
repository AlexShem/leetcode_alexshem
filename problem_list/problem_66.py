def plus_one(digits: list[int]) -> list[int]:
        number = int(''.join([str(d) for d in digits]))
        return [int(dig) for dig in str(number + 1)]
    
if __name__ == "__main__":
    digits = [1,2,3]
    # Output: [1,2,4]
    print(plus_one(digits))