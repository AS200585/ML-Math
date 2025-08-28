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