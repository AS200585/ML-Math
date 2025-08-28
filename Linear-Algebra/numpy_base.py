import numpy as np

num_list = [2, 4, 5, 7, 10, 13]

# Find the absolute value
# Absolute value refers to the distance of a number from zero
print(abs(-5))

# Find the maximum value
print(max(num_list))

# Find the minimum value
print(min(num_list))

# Find the sum
print(sum(num_list))

# Find the average
print("average:", sum(num_list) / len(num_list))

# Find the mean 
print("statistical mean:", np.mean(num_list))

# Find the median
print("statistical median:", np.median(num_list))

# Find the standard deviation
print("statistical standard deviation:", np.std(num_list)) 

# Find the square
print("statistical square:", np.square(num_list))

# Find the cube root
print("statistical cube root:", np.cbrt(num_list))

# Find the Linear Space
# A Linear Space is a collection of points that are evenly distributed between two endpoints.
# It is often used in mathematics and physics to describe a range of values.
# For example, the linear space between 0 and 1 with 5 points is:
print("statistical linear space:", np.linspace(-4, 12, 20))

# Find the Linear Algebra
# Linear Algebra is a branch of mathematics concerning linear equations, linear functions, and their representations through matrices and vector spaces.
# It is a foundational area of mathematics with applications in various fields, including physics, computer science, and engineering.
# For example, linear algebra is used in computer graphics to manipulate images and in machine learning to optimize algorithms.
print("Linear Algebra: \n", np.linalg.cholesky(np.eye(3)))
# np.eye creates a 2-D array with ones on the diagonal and zeros elsewhere.
# cholesky decomposition is a method for solving linear equations and is used in various applications, including optimization and machine learning.
print("Linear Algebra 2: \n", np.linalg.inv(np.eye(7)))
# inv computes the inverse of a matrix.


func_output = np.linspace(-19, 33, 29)
print("Function Output: \n",func_output + 2)