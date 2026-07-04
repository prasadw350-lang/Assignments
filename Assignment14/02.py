# Import NumPy
import numpy as np
# Generate 1D 20 random integers between 1 and 50
arr = np.random.randint(1, 51, 20)
print("Array:")
print(arr)
# Statistics
print("\nMinimum Value:", np.min(arr))
print("Index of Minimum:", np.argmin(arr))
print("\nMaximum Value:", np.max(arr))
print("Index of Maximum:", np.argmax(arr))
print("\nSum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))

