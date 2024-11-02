def is_happy(n: int) -> bool:
    def n_tranform(number: int) -> int:
        result = 0
        while number:
            result += (number % 10) ** 2
            number //= 10
        return result
    
    passed = set()
    
    while n not in passed:
        passed.add(n)
        n = n_tranform(n)
        if n == 1:
            return True
    return False
    
    

if __name__ == "__main__":
    # n = 19
    # Output: true
    
    n = 2
    # Output: false
    
    print(is_happy(n))