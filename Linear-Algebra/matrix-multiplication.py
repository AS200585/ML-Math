# Matrix Multiplication
"""
Matrix multiplication is a fundamental operation in linear algebra, used in various applications such as computer graphics, 
machine learning, and scientific computing. 
In this example, we will demonstrate how to perform matrix multiplication using Python with the NumPy library.

Matrix multiplication is not the same as element-wise multiplication.
For two matrices A and B to be multiplied, the number of columns in A must equal the number of rows in B.
The resulting matrix will have the number of rows of A and the number of columns of B.

Key points:
- If A is of shape (m, n) and B is of shape (n, p), the resulting matrix C will be of shape (m, p).
- The element C[i][j] in the resulting matrix is computed as the dot product of the i-th row of A and the j-th column of B.
- We can use the `numpy.dot()` function or the `@` operator for matrix multiplication in NumPy.
- NumPy also provides the `numpy.matmul()` function for matrix multiplication.
- For 1-D arrays, the dot product is equivalent to the inner product of vectors.
- For 2-D arrays, it is equivalent to matrix multiplication.
- For N-D arrays, it is a sum product over the last axis of the first array and the second-to-last axis of the second array.
- Broadcasting is not supported, but the function can handle inputs of different dimensions.
- The function can also handle stacks of matrices.
- The function supports complex numbers and can handle conjugation when specified.
- The function can be used with both contiguous and non-contiguous arrays.
- The function can be used with arrays of different memory layouts (C-contiguous and F-contiguous) and of different memory orders (C-order and F-order).
- The function can be used with arrays of different shapes, as long as the dimensions are compatible for matrix multiplication.
- The function can be used with arrays of different data types, as long as they are compatible for the operation.
- The function can be used with arrays of different sizes, different ranks, different strides, and different alignments, 
  as long as they are compatible for the operation.

Example:
Consider two matrices A and B:
A = [[1, 2, 3],
     [4, 5, 6]]
B = [[7, 8],
     [9, 10],
     [11, 12]]
     
The product of A and B is:
C = [[58, 64],
     [139, 154]]

A - m X n, B - n X p
Therefore, C - m X p
"""

import numpy as np

M1 = np.random.randn(3, 9)
M2 = np.random.randn(4, 9)

M2_T = np.transpose(M2)  # Transpose M2 to make it (9, 4) for multiplication

print("Matrix 1 : \n", M1)
print("Matrix 2 : \n", M2)
print("Transposed Matrix 1 : \n", M1.T)
print("Transposed Matrix 2 : \n", M2_T)

M3 = np.matmul(M1, M2_T)  # Matrix multiplication (3x9) . (9x4) = (3x4)
print("Matrix Multiplication(Matrix 3) : \n", M3)
print("@ Function : \n", M1 @ M2_T)  # Using @ operator for matrix multiplication

print("Difference : \n", M3 - (M1 @ M2_T))
print("Sum : \n", M3 + (M1 @ M2_T))
print("Multiplication : \n", M3 * (M1 @ M2_T))
print("Equal Matrix? ", np.array_equal(M3, (M1 @ M2_T)))  