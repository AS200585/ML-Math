# Vector Dot Product

"""
A vector dot product is a fundamental operation in linear algebra that takes two equal-length sequences of numbers 
(usually coordinate vectors) and returns a single number. 
Dot Product is one of the most important operations in Linear Algebra.
This operation is widely used in various applications, including physics, computer graphics, and machine learning.

The equation is : a . b = |a| |b| cos(θ)

Dot Product is a scalar value that is the result of multiplying two vectors.
It is indicated by the dot symbol (·) and is calculated as the sum of the products of the corresponding entries of the two sequences of numbers.
It is also indicated using A(^T)B      ^T : Transpose

In dot product, we make sure that two or more vectors are of the same dimensionality.
Then, we multiply each of the corresponding elements of the vectors and sum the results.

A vector is orthogonal to another vector if their dot product is zero and both vectors are non-zero.
"""

import numpy as np

vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])
dot_product = np.dot(vector1, vector2) # np.dot from NumPy is a function that computes the dot product of two arrays.
print("Dot Product 1:", dot_product)

vector3 = np.array([-3, 4, -19])
vector4 = np.array([2, -9, 5])
dot_product2 = np.dot(vector3, vector4)
print("Dot Product 2:", dot_product2)

vector0 = np.array([0, 0, 0])  # A vector will all zeros in Linear Algebra is called Zeros Vector
dot_product0 = np.dot(vector1, vector0)
print("Dot Product - Zeros Vector:", dot_product0)