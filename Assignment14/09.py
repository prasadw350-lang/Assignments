# Import NumPy
import numpy as np
# Generate 6x6 matrix
arr = np.random.randn(6,6)
print("Original Matrix:")
print(arr)

# Properties
print("\nShape:", arr.shape)
print("Size:", arr.size)
print("Data Type:", arr.dtype)
# Index of maximum and minimum values
print("\nIndex of Maximum Value:")
print(np.unravel_index(np.argmax(arr), arr.shape))
print("\nIndex of Minimum Value:")
print(np.unravel_index(np.argmin(arr), arr.shape))
# Top-left 3x3 submatrix
print("\nTop-left 3x3 Submatrix:")
print(arr[:3,:3])

# Replace negative values with absolute values
arr = np.abs(arr)
print("\nModified Matrix:")
print(arr)
# Mean
print("\nMean:", np.mean(arr))

