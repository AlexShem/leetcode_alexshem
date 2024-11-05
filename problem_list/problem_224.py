from collections import deque

operator_precedence = {
    "(": 4,
    ")": 4,
    "*": 3,
    "/": 3,
    "+": 2,
    "-": 2,
    # 4: '()',  # Parentheses
    # 3: '*/',  # Binary multiplication and division
    # 2: '+-',  # Binary plus and minus
    # 1: '',  # Reserved
}

operator_list = '+-*/()'


def to_reverse_polish_notation(s: str) -> list[str]:
    output = []
    operator_stack = deque([])

    for token in s:  # Assumes there a number can only be a digit
        if token.isnumeric():
            output.append(token)
        elif token in '+-*/':
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
            elif token == '*':
                stack.append(operand_1 * operand_2)
            elif token == '/':
                stack.append(operand_1 / operand_2)
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
