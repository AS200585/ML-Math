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
"""