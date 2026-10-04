import numpy as np
import matplotlib.pyplot as plt

# Use numpy to create an array
arr = np.array([1, 2, 3, 4, 5])
print("Numpy array:", arr)

# Use matplotlib to plot a simple graph
plt.plot(arr, arr ** 2)
plt.title("Sample Plot")
plt.show()
