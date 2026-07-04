# Import NumPy
import numpy as np
# Create 1D array from 1 to 24
arr = np.arange(1, 25)
print("Original Array:")
print(arr)
# Reshape into (4,6)
arr1 = arr.reshape(4, 6)
print("\n4 x 6 Array:")
print(arr1)
print("Shape:", arr1.shape)
# Reshape into (3,8)
arr2 = arr.reshape(3, 8)
print("\n3 x 8 Array:")
print(arr2)
print("Shape:", arr2.shape)
# Reshape into (2,3,4)
arr3 = arr.reshape(2, 3, 4)
print("\n2 x 3 x 4 Array:")
print(arr3)
print("Shape:", arr3.shape)

