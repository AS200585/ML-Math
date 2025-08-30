import matplotlib.pyplot as plt
import numpy as np

# Example 1
x = np.arange(-24, 26)
print(x)
y = np.linspace(-19, 21, 50)
print(y)
plt.plot(x, y, 'o')
plt.show()

# Example 2
x2 = np.arange(-4, 5)
y2 = x2**4 + x2*-2
plt.plot(x2, y2, 'r')
plt.plot(x2, y2/2, 'gs') # for additional points on same graph
plt.show()

# Example 3 - Plotting a Straight Line only
plt.plot([-2, 5], [-1, 1], 'k-', label='first line')
plt.plot([-1, 0], [-3, 2], 'g-', label='second line')
plt.legend() # Add a legend to show which line is which using the labels and colors
plt.show()

# Example 4 - Visualize Images
img = np.random.randint(-3, 19, size=(8, 9))
print(img)
plt.imshow(img)
plt.colorbar() # Show a color scale
plt.show() 
# This displays the image with the color scale that corresponds to the values of each element of the matrix as colors