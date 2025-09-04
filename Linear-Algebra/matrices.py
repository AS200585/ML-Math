# Matrices

"""
Matrices are two-dimensional arrays of numbers, symbols, or expressions, arranged in rows and columns.
They are a fundamental concept in linear algebra and are used to represent and solve systems of linear equations.
In machine learning, matrices are used to represent datasets, where each row corresponds to a data point and each column corresponds to a feature.

Operations on matrices, such as addition, subtraction, and multiplication, are essential for various algorithms, 
including linear regression, neural networks, and more.

Diagonal matrices are a special type of matrix where the entries outside the main diagonal are all zero. Only diagonal elements are non-zero.
Ones matrices are matrices where all the elements are equal to one.
Zeros matrices are matrices where all the elements are equal to zero.

Diagonal of a matrix refers to the entries that extend from the top left corner to the bottom right corner.
All numbers outside the diagonal are considered off-diagonal elements.

Symmetric matrices are square matrices that are equal to their transpose.
In other words, a matrix A is symmetric if A = A^T. In this matrix, 
the element at row i and column j is equal to the element at row j and column i.
2 or more symmetric matrices can be added or subtracted to produce another symmetric matrix.
Also, all the elements above the main diagonal are equal to their corresponding elements below the diagonal.

Identity matrices are square matrices with ones on the main diagonal and zeros elsewhere. It is denoted as I_n, where n is the size of the matrix.
"""


import numpy as np

I = np.eye(7)  # Identity matrix of size 7x7
D = np.diag([1, 2, 3])  # Diagonal matrix
O = np.ones((2, 3))  # Ones matrix of size 2x3
Z = np.zeros((3, 2))  # Zeros matrix of size 3x2
A = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])  # Example matrix (4x2)

# For symmetric matrix, it must be square (n x n)
symmetric_A = np.array([[1, 2, 3], 
                       [2, 4, 5], 
                       [3, 5, 6]])  # Symmetric 3x3 matrix

# Create a square matrix from A for operations that require square matrices
A_square = np.array([[1, 2], [3, 4]])  # 2x2 matrix for inverse, determinant, etc.

diagonal_A = np.diag(np.diag(A_square))  # Diagonal of square matrix A
transpose_A = A.T  # Transpose of matrix A

# Matrix addition/subtraction requires same dimensions
# Create another 4x2 matrix for addition/subtraction
B = np.array([[2, 1], [1, 2], [3, 2], [2, 3]])  # 4x2 matrix
matrix_addition = A + B  # Matrix addition
matrix_subtraction = A - B  # Matrix subtraction

# Matrix multiplication: (m x n) * (n x p) = (m x p)
# A is 4x2, so we need a 2x3 matrix for multiplication
C = np.array([[1, 2, 3], [4, 5, 6]])  # 2x3 matrix
matrix_multiplication = np.dot(A, C)  # Matrix multiplication (4x2 * 2x3 = 4x3)

# Element-wise multiplication requires same dimensions
elementwise_multiplication = A * B  # Element-wise multiplication

# Inverse and determinant require square matrices
matrix_inverse = np.linalg.inv(A_square)  # Inverse of square matrix A
determinant_A = np.linalg.det(A_square)  # Determinant of square matrix A

rank_A = np.linalg.matrix_rank(A)  # Rank of matrix A

# Eigenvalues/eigenvectors require square matrices
eigenvalues_A, eigenvectors_A = np.linalg.eig(A_square)  # Eigenvalues and eigenvectors

full_matrix = np.full([10, 6], 42)  # Full matrix of size 10x6 with all elements as 42

print("Identity Matrix:\n", I)
print("\nDiagonal Matrix:\n", D)
print("\nOnes Matrix:\n", O)
print("\nZeros Matrix:\n", Z)
print("\nMatrix A (4x2):\n", A)
print("\nSymmetric Matrix (3x3):\n", symmetric_A)
print("\nSquare Matrix A (2x2):\n", A_square)
print("\nDiagonal of Square Matrix A:\n", diagonal_A)
print("\nTranspose of Matrix A:\n", transpose_A)
print("\nMatrix Addition (A + B):\n", matrix_addition)
print("\nMatrix Subtraction (A - B):\n", matrix_subtraction)
print("\nMatrix Multiplication (A * C):\n", matrix_multiplication)
print("\nElement-wise Multiplication (A * B):\n", elementwise_multiplication)
print("\nInverse of Square Matrix A:\n", matrix_inverse)
print(f"\nDeterminant of Square Matrix A: {determinant_A:.4f}")
print(f"\nRank of Matrix A: {rank_A}")
print(f"\nEigenvalues of Square Matrix A: {np.around(eigenvalues_A, decimals=4)}")
print(f"\nEigenvectors of Square Matrix A:\n{np.around(eigenvectors_A, decimals=4)}")
print("\nFull Matrix:\n", full_matrix)