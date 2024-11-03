def solve_equation(equation: str) -> str:
    # Helper function to split and collect coefficients from an expression
    def collect_coefficients(expression: str) -> (int, int):
        terms = []
        term = ""
        for char in expression:
            if char in "+-":
                if term:
                    terms.append(term)
                term = char
            else:
                term += char
        terms.append(term)

        x_coefficient = 0
        constant = 0

        for term in terms:
            if "x" in term:
                if term == "x" or term == "+x":
                    x_coefficient += 1
                elif term == "-x":
                    x_coefficient -= 1
                else:
                    x_coefficient += int(term.replace("x", ""))
            else:
                constant += int(term)

        return x_coefficient, constant

    # Split equation into LHS and RHS
    lhs, rhs = equation.split('=')
    lhs_x, lhs_const = collect_coefficients(lhs)
    rhs_x, rhs_const = collect_coefficients(rhs)

    # Bring all x terms to the left and constants to the right
    total_x = lhs_x - rhs_x
    total_const = rhs_const - lhs_const

    # Determine the solution
    if total_x == 0:
        if total_const == 0:
            return "Infinite solutions"
        else:
            return "No solution"

    # Calculate the value of x
    x_value = total_const // total_x
    return f"x={x_value}"


# Testing the function
if __name__ == "__main__":
    # Test 1
    eq = "x+5-3+x=6+x-2"
    print(solve_equation(eq))  # Output: "x=2"

    # Test 2
    eq = "x=x"
    print(solve_equation(eq))  # Output: "Infinite solutions"

    # Test 3
    eq = "2x=x"
    print(solve_equation(eq))  # Output: "x=0"
