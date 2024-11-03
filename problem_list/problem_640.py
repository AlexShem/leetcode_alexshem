def solve_equation(equation: str) -> str:
    def split_terms(expression: str) -> list[str]:
        terms = []
        term = "+"
        # Special treatment of the first character:
        # If it is a unary sign ('-')
        if expression[0] == '-':
            term = '-'
            expression = expression[1:]

        for char in expression:
            if char == '+' or char == '-':
                terms.append(term)
                term = char
            else:
                term += char
        terms.append(term)
        return terms

    def collect_terms(terms: list[str]) -> list[str]:
        x_coefficient = 0
        constant = 0
        for term in terms:
            x_index = term.find("x")
            if x_index == 0:
                x_coefficient += 1
            elif x_index == 1:  # "2x" or "+x" or "-x"
                coefficient = term[0]
                if coefficient == '+':
                    x_coefficient += 1
                elif coefficient == '-':
                    x_coefficient -= 1
                else:
                    x_coefficient += int(coefficient)
            elif x_index > 1:
                x_coefficient += int(term[:x_index])
            else:
                constant += int(term)

        term_x = "+" + str(x_coefficient) + "x" if x_coefficient >= 0 else str(x_coefficient) + "x"
        term_const = "+" + str(constant) if constant >= 0 else str(constant)
        return [term_x, term_const]

    lhs, rhs = equation.split('=')
    lhs_terms = split_terms(lhs)
    rhs_terms = split_terms(rhs)
    lhs_terms = collect_terms(lhs_terms)
    rhs_terms = collect_terms(rhs_terms)

    # Move all "x" terms to left and all contant terms to right
    coefficient_x = int(lhs_terms[0].replace("x", "")) - int(rhs_terms[0].replace("x", ""))
    coefficient_c = int(rhs_terms[1]) - int(lhs_terms[1])

    # Check if the solution exist
    if coefficient_x == 0:
        if coefficient_c == 0:
            return "Infinite solutions"
        else:
            return "No solution"

    # Check that the solution is an integer
    if coefficient_c % coefficient_x != 0:
        return "No solution"

    x_solution = coefficient_c // coefficient_x

    return "x=" + str(x_solution)


if __name__ == "__main__":
    # Test 1
    eq = "x+5-3+x=6+x-2"
    # Output: "x=2"
    print(solve_equation(eq))

    # Test 2
    eq = "x=x"
    # Output: "Infinite solutions"
    print(solve_equation(eq))

    # Test 3
    eq = "2x=x"
    # Output: "x=0"
    print(solve_equation(eq))
