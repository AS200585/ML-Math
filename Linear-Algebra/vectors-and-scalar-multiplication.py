# Vectors and Scalar Multiplication

"""
Vectors is a mathematical object that has both magnitude and direction. 
Vectors are also called and ordered lists of numbers.
They are often represented as arrows in a coordinate system, with the length of the arrow indicating 
the magnitude and the direction of the arrow indicating the direction.
These arrows can be added together or multiplied by a scalar to produce new vectors.

Vectors can be represented in component form, such as (x, y, z), where each component corresponds to a dimension in space.
These components can be manipulated using various mathematical operations, such as addition, subtraction, and scalar multiplication.
Vectors can be represented in matrix form, where each column represents a different vector.
Vectors can also be represented as a single column or row in a matrix, depending on the context.

Vectors can have different orientations - they can be column vectors or row vectors.
Column vectors are represented as a single column of values, while row vectors are represented as a single row of values. 
This is the algebraic interpretation is important when performing operations like matrix multiplication.
There is also a geometric interpretation of vectors, which considers their direction and magnitude in space.
This geometric interpretation is important for understanding concepts like vector addition and scalar multiplication.

Vector-Scalar Multiplication: W = λ x v(vector)
When Lambda (λ) is a scalar and v is a vector, the result of multiplying them is a new vector W.
λ > 1 means stretching the vector in the direction of its components, while λ < 1 means compressing it.
λ = 1 means the vector remains unchanged, and λ = 0 results in the zero vector.
λ < 0 means the vector is flipped in the opposite direction.

In AIML, vectors are used to represent various types of data, such as word embeddings, image features, and more. 
They play a crucial role in machine learning algorithms, particularly in the areas of natural language processing and computer vision.
"""
"""
Dimensionality is the number of components or coordinates needed to specify a point in a space.
It also refers to the number of features or attributes in a dataset, the number of columns in a data table, the number of dimensions 
in a geometric space, and also the number of elements in a vector.

In the context of vectors, it refers to the number of dimensions in which the vector exists.
For example, a 2D vector has two components (x, y), while a 3D vector has three components (x, y, z).

Higher-dimensional vectors can exist in spaces with more than three dimensions, which are often used in machine learning and data analysis.
"""

import matplotlib.pyplot as plt
import numpy as np

vector = [3, 4, 5]  # vector
s = 2               # scalar
print(vector*s)  # scalar multiplication
# The output is python repeating this vector twice - [3, 4, 5, 3, 4, 5]
# This is not the desired behavior for vector-scalar multiplication. Python does not treat it as a vector.
# This means that the vector will repeat n number of times (where n is the scalar).

vector2 = np.array([3, 4, 5])  # vector
print(vector2*s)               # scalar multiplication
# The output is [6 8 10], which is the desired behavior for vector-scalar multiplication.
# Python treats numpy arrays as vectors, allowing for element-wise operations.

vec2d = np.array([8, 9])
s1 = 2
s2 = 0.27
s3 = -3.5

plt.plot([0, vec2d[0]], [0, vec2d[1]], marker='s', label='Original Vector', color='r')  # Original vector in red
plt.plot([0, vec2d[0]*s1], [0, vec2d[1]*s1], marker='o', label='Scaled by s1', color='g')  # Scaled by 2 in green
plt.plot([0, vec2d[0]*s2], [0, vec2d[1]*s2], marker='^', label='Scaled by s2', color='b')  # Scaled by 0.27 in blue
plt.plot([0, vec2d[0]*s3], [0, vec2d[1]*s3], marker='v', label='Scaled by s3', color='y')  # Scaled by -3.5 in yellow
plt.legend()
plt.axis('equal')  # Equal scaling for both axes
plt.xlim(-10, 10)  # Puts x-axis limits
plt.ylim(-10, 10)  # Puts y-axis limits
plt.grid()
plt.title('Vector and Scalar Multiplication')
plt.show()


"""
TASK
- Create two vectors(2D)
- Plot each vector
- Plot v1+v2, v1-v2, v1*4 + v2/2
"""

vec1 = np.array(np.random.randint(1, 10, size=2))
vec2 = np.array(np.random.randint(1, 10, size=2))
print(vec1)
print(vec2)

vec_sum = vec1 + vec2
vec_diff = vec1 - vec2
vec_combined = vec1 * 4 + vec2 / 2

plt.plot([0, vec1[0]], [0, vec1[1]], marker='o', label='Vector 1', color='r')  # Vector 1 in red
plt.plot([0, vec2[0]], [0, vec2[1]], marker="s", label='Vector 2', color='g')  # Vector 2 in green
plt.plot([0, vec_sum[0]], [0, vec_sum[1]], marker='o', label='Vector 1', color='gold')  # Vector Sum in gold
plt.plot([0, vec_diff[0]], [0, vec_diff[1]], marker="s", label='Vector 2', color='grey')  # Vector Difference in grey
plt.plot([0, vec_combined[0]], [0, vec_combined[1]], marker='o', label='Vector 1', color='blue')  # Vector Equation in blue
plt.legend()
plt.grid()
plt.show()