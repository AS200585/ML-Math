# Matrix Inverse Concepts

"""
Matrix inversion is a fundamental operation in linear algebra, used to find a matrix that, 
when multiplied by the original matrix, yields the identity matrix.
Matrix inversion is widely used in various applications such as solving systems of linear equations, computer graphics, machine learning, and more.
For example, in machine learning, the inverse of a matrix is often used in algorithms like linear regression to compute the 
coefficients of the model.

Key points:
- A square matrix A is invertible (or non-singular) if there exists a matrix B such that AB = BA = I, where I is the identity matrix.
- Not all matrices are invertible. A matrix is invertible if and only if its determinant is non-zero.
- The inverse of a matrix A is denoted as A^(-1).
- The inverse of a product of matrices is the product of their inverses in reverse order: (AB)^(-1) = B^(-1)A^(-1).
- The inverse of a transpose of a matrix is the transpose of the inverse: (A^T)^(-1) = (A^(-1))^T.
- The inverse of a scalar multiple of a matrix is the reciprocal of the scalar times the inverse of the matrix: (cA)^(-1) = (1/c)A^(-1), for c ≠ 0.
- The inverse of the identity matrix is the identity matrix itself: I^(-1) = I.
- The inverse of an orthogonal matrix is its transpose: if A is orthogonal, then A^(-1) = A^T.
- The inverse of a diagonal matrix is obtained by taking the reciprocal of each non-zero element on the diagonal.
- If AX = B, then A^(-1)AX = A^(-1)B 
- Similarly, IX = A^(-1)B
- The inverse of a 2x2 matrix can be computed using the formula:
  A = [[a, b],
       [c, d]]
  A^(-1) = (1/det(A)) * [[d, -b],
                          [-c, a]]
  where det(A) = ad - bc is the determinant of A.
- For larger matrices, the inverse can be computed using methods such as Gaussian elimination, LU decomposition, or using numerical libraries.
- In Python, the NumPy library provides a convenient function `numpy.linalg.inv()` to compute the inverse of a matrix.

For a fraction, a/b, the inverse is b/a. Or in other words, the inverse of a number is 1 divided by that number.
If S/R is a fraction, then its inverse is R/S or SR^(-1).
For example, the inverse of 2/3 is 3/2 or 2^(-1) * 3 or 2 * 3^(-1).

Matrix inverse is necessary for solving systems of linear equations of the form Ax = b, where A is a matrix, 
x is a vector of variables, and b is a vector of constants.
The solution can be found using the inverse of A: x = A^(-1)b, provided that A is invertible.
"""

import numpy as np
import matplotlib.pyplot as plt

M = np.random.randint(1, 10, (5, 5))
M_inv = np.linalg.inv(M)

print("Matrix : \n", M) 
print("Inverse Matrix : \n", M_inv)
print("Product of Matrix and its Inverse (Identity Matrix) : \n", M @ M_inv)
print("Determinant of the Matrix : \n", np.linalg.det(M))  # Determinant of the matrix
print("Determinant of the Inverse Matrix : \n", np.linalg.det(M_inv))  # Determinant of the inverse matrix
print("Product of Determinants : \n", np.linalg.det(M) * np.linalg.det(M_inv))  # Product of determinants
print("Inverse of Transpose of the Matrix : \n", np.linalg.inv(M.T))  # Inverse of the transpose of the matrix
print("Transpose of the Inverse of the Matrix : \n", M_inv.T)  # Transpose of the inverse of the matrix

fig, axis = plt.subplots(1, 3, figsize=(12, 12)) #subplots(rows, columns, figsize=(width, height))
axis[0].imshow(M, cmap='gray')
axis[0].set_title("Original Matrix")
axis[1].imshow(M_inv, cmap='copper_r')
axis[1].set_title("Inverse Matrix : A$^{-1}$") # $^{-1}$ is for superscript -1
# we put $ around -1 to indicate that it is LaTeX math mode
axis[2].imshow(M @ M_inv, cmap='Dark2_r')
axis[2].set_title("Product of Matrix and Inverse : I (A$^{-1}$A)")
plt.show()