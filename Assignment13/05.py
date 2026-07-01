# Import NumPy
import numpy as np
# a) Random numbers between 0 and 1
array1 = np.random.rand(10)
# b) Random numbers from standard normal distribution
array2 = np.random.randn(3, 3)
# c) Random integers between 10 and 50
array3 = np.random.randint(10, 51, (4, 5))

# Display arrays
print("Random Numbers (0 to 1):")
print(array1)
print("\n3x3 Standard Normal Matrix:")
print(array2)
print("\n4x5 Random Integer Matrix:")
print(array3)

