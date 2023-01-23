import numpy as np

if __name__ == "__main__":
    # Print a specific 3x3 matrix where a cell is 1 if i == j, else 0
    matrix_1 = np.array([[1 if i == j else 0 for j in range(3)] for i in range(3)])
    print(str(matrix_1).replace(' [', '').replace('[', '').replace(']', ''))
    print()

    # Print the 3x3 matrix from #1 and then add 3 to every cell where i ≠ j
    matrix_2 = np.where(matrix_1 != 1, matrix_1 + 3, matrix_1)
    print(str(matrix_2).replace(' [', '').replace('[', '').replace(']', ''))
    print()

    # Print the 3x3 matrix from #2 as a 3x2 by deleting the last column from the matrix created
    matrix_3 = np.delete(matrix_2, 2, 1)
    print(str(matrix_3).replace(' [', '').replace('[', '').replace(']', ''))