# Transposing Vectors and Matrices

"""
Transposing is an operation that flips a matrix over its diagonal, switching the row and column indices of the matrix.
For a given matrix A, its transpose is denoted as A^T. If A is an m x n matrix, then A^T will be an n x m matrix.
For example, if we have a matrix A:
A = [[1, 2, 3],
    [4, 5, 6]]

Then its transpose A^T will be:
A^T = [[1, 4],
      [2, 5],
      [3, 6]]

Key properties of matrix transpose include:
- The transpose of the transpose: (A^T)^T = A
- Transpose of a sum: (A + B)^T = A^T + B^T
- Transpose of a product: (AB)^T = B^T A^T
- For square matrices, if A^T = A, the matrix is symmetric; if A^T = -A, it is skew-symmetric.
- For real matrices, the transpose of a matrix is equivalent to its conjugate transpose.
- For symmetric matrices, the transpose is the same as the original matrix.
- The transpose of an identity matrix, diagonal matrix, zero matrix and ones matrix is itself.
- The transpose of a product of matrices is the product of their transposes in reverse order.
- The transpose of a scalar multiple of a matrix is the scalar multiple of the transpose of the matrix.
- The transpose of a matrix does not change its rank.
- The transpose of an orthogonal matrix is also its inverse.
- The transpose of a Hermitian matrix is equal to its complex conjugate.


In the case of vectors, transposing a row vector converts it into a column vector and vice versa.
For instance, a row vector v = [1, 2, 3] becomes a column vector v^T = [[1], [2], [3]] after transposition.
This is crucial in vector operations, such as dot products, where the transpose ensures compatibility.

Transposing is particularly useful in various mathematical and computational applications, including solving systems of linear equations, 
computer graphics (e.g., transformations), and machine learning (e.g., in neural networks for weight matrices).
In Python, libraries like NumPy provide efficient implementations: np.transpose(A) or A.T for matrices.

"""

import numpy as np

v1 = np.array([-1, 2, -3])
print("Original Vector:", v1)
print("Transposed Vector:", v1.T) # Transpose of vector (row to column or vice versa)
# Note: For 1D arrays, .T has no effect. To see the effect, we need to make it 2D.
v1_2d = np.array([-1, 2, -3], ndmin=2)  # Making it a 2D array (1x3)
print("2D Original Vector:\n", v1_2d)
print("2D Transposed Vector:\n", v1_2d.T)

M1 = np.random.randn(3, 5)  # Example matrix (3x4)
print("Original Matrix:\n", np.around(M1, decimals=3))
print("Transposed Matrix:\n", np.around(M1.T, decimals=3))  # Transpose of matrix

M2 = np.round(10*np.random.randn(7, 4), decimals=3)  # Another example matrix (7x4)
print("Original Matrix M2:\n", M2)
print("Transposed Matrix M2:\n", M2.T)