def solve_equation(equation: str) -> str:
    """Solves a linear equation for 'x' and returns the result.

    The equation contains only '+' and '-' operations, the variable 'x', and its coefficient.
    Possible outputs are:

    - "x=#value": If there is a single integer solution.
    - "Infinite solutions": If there are infinite possible values for 'x'.
    - "No solution": If no value of 'x' can satisfy the equation.

    :param equation: A string representing the linear equation.
    :type equation: str
    :return: A string representing the solution of the equation.
    :rtype: str
    """

    def collect_coefficients(expression: str) -> tuple[int, int]:
        """Splits an expression into individual terms and collects the coefficients for 'x' and the constants.

        :param expression: A string representing part of the equation (left-hand side or right-hand side).
        :type expression: str
        :return: A tuple containing the coefficient of 'x' and the constant.
        :rtype: tuple(int, int)
        """
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

    # Split the equation into left-hand side (LHS) and right-hand side (RHS)
    lhs, rhs = equation.split('=')
    lhs_x, lhs_const = collect_coefficients(lhs)
    rhs_x, rhs_const = collect_coefficients(rhs)

    # Bring all 'x' terms to the left and all constant terms to the right
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
    print(solve_equation(eq))  # Expected output: "x=2"

    # Test 2
    eq = "x=x"
    print(solve_equation(eq))  # Expected output: "Infinite solutions"

    # Test 3
    eq = "2x=x"
    print(solve_equation(eq))  # Expected output: "x=0"
