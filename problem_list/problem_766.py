def is_toeplitz_matrix(matrix: list[list[int]]) -> bool:
    def extract_diagonal(mat: list[list[int]], index: int):
        n, m = len(mat), len(mat[0])
        diagonal = []
        i = 0 if index >= 0 else -index
        j = index if index >= 0 else 0

        while i < n and j < m:
            diagonal.append(mat[i][j])
            i += 1
            j += 1
        return diagonal

    lower_diags = len(matrix) - 1
    upper_diags = len(matrix[0]) - 1
    diags = range(-lower_diags, upper_diags, 1)

    for daig_ind in diags:
        diag = extract_diagonal(matrix, daig_ind)
        if not all(x == diag[0] for x in diag):
            return False

    return True
