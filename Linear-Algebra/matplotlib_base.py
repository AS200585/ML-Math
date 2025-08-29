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
plt.show()