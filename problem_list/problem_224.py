from collections import deque

operator_precedence = {
    "(": 4,
    ")": 4,
    "~": 3,
    "*": 2,
    "/": 2,
    "+": 1,
    "-": 1,
}

operator_list = '+-*/()'


def tokenize_string(s: str) -> list[str]:
    tokens = []
    i = 0

    while i < len(s):
        char = s[i]
        if char.isdigit():
            num = char
            i += 1
            while i < len(s) and s[i].isdigit():
                num += s[i]
                i += 1
            tokens.append(num)
            continue
        elif char == '-':
            if i == 0 or (i > 0 and s[i - 1] == '('):
                tokens.append('~')
            else:
                tokens.append('-')
        elif char in '+*/()':
            tokens.append(char)
        i += 1
    return tokens


def to_reverse_polish_notation(s: str) -> list[str]:
    output = []
    s_tokenized = tokenize_string(s)
    operator_stack = deque([])

    for token in s_tokenized:
        if token.isnumeric():
            output.append(token)
        elif token in '+-*/~':
            while len(operator_stack) and operator_stack[-1] != '(' and (
                    operator_precedence[operator_stack[-1]] >= operator_precedence[token]):
                output.append(operator_stack.pop())

            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            if operator_stack[-1] != '(':
                raise ValueError("Mismatch of the parenthesis detected.")
            operator_stack.pop()
    while len(operator_stack):
        output.append(operator_stack.pop())

    return output


def evaluate_from_rpn(rpn_stack: list[str]) -> int:
    stack = deque([])

    for token in rpn_stack:
        if token.isnumeric():
            stack.append(int(token))
        elif token in '+-*/':
            operand_2 = stack.pop()
            operand_1 = stack.pop()
            if token == '+':
                stack.append(operand_1 + operand_2)
            elif token == '-':
                stack.append(operand_1 - operand_2)
            elif token == '-':
                stack.append(operand_1 - operand_2)
            elif token == '*':
                stack.append(operand_1 * operand_2)
            elif token == '/':
                stack.append(operand_1 / operand_2)
        elif token == '~':
            operand = stack.pop()
            stack.append(-operand)
    return stack.pop()


def calculate(s: str) -> int:
    s = s.strip().replace(" ", "")
    s_rpn = to_reverse_polish_notation(s)

    out = evaluate_from_rpn(s_rpn)
    return out


if __name__ == "__main__":
    expression = "1 + 1"
    result = calculate(expression)  # Expected Output: 2
    print(result)

    expression = " 2-1 + 2 "
    result = calculate(expression)  # Expected Output: 3
    print(result)

    expression = "(1+(4+5+2)-3)+(6+8)"
    result = calculate(expression)  # Expected Output: 23
    print(result)

    expression = "-(2+1)"
    result = calculate(expression)  # Expected Output: -3
    print(result)

    expression = "2147483647"
    result = calculate(expression)  # Expected Output: 2147483647
    print(result)

    expression = "1-(     -2)"
    result = calculate(expression)  # Expected Output: 3
    print(result)
