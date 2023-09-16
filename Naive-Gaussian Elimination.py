def forward_elimination(matrix, n):
    for row in range(n):
        pivot_row = row
        for i in range(row + 1, n):
            if abs(matrix[i][row]) > abs(matrix[pivot_row][row]):
                pivot_row = i
        # Swap the pivot row with the current row (if necessary)
        if pivot_row != row:
            matrix[row], matrix[pivot_row] = matrix[pivot_row], matrix[row]
        
        # Make the diagonal element 1
        pivot_element = matrix[row][row]
        for j in range(row, n + 1):
            matrix[row][j] /= pivot_element
        
        # Eliminate other rows
        for i in range(row + 1, n):
            factor = matrix[i][row]
            for j in range(row, n + 1):
                matrix[i][j] -= factor * matrix[row][j]

def back_substitution(matrix, n):
    solution = [0] * n
    for row in range(n - 1, -1, -1):
        solution[row] = matrix[row][n]
        for j in range(row + 1, n):
            solution[row] -= matrix[row][j] * solution[j]
    return solution

def gauss_elimination(matrix):
    n = len(matrix)
    forward_elimination(matrix, n)
    return back_substitution(matrix, n)

def get_user_input():
    n = int(input("Enter the number of linear equations: "))
    matrix = []
    for i in range(n):
        equation = input(f"Enter coefficients of equation {i+1} separated by spaces, followed by the constant value: ").split()
        matrix.append([float(x) for x in equation])
    return matrix

def format_output(value):
    return format(value, ".6f")

if __name__ == "__main__":
    # Get user input for the system of equations
    A = get_user_input()

    # Perform Gaussian elimination
    solution = gauss_elimination(A)

    # Print the solution
    print("\nSolution:")
    for i, x in enumerate(solution):
        formatted_x = format_output(x)
        print(f"x{i+1} = {formatted_x}")