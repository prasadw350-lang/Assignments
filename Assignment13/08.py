# Import NumPy 
import numpy as np

# Create a 4x4 random matrix
matrix = np.random.randint(1, 101, (4,4))
print("Matrix:")

print(matrix)
print("\nShape:", matrix.shape)
print("Dimension:", matrix.ndim)
print("Total Elements:", matrix.size)
print("Data Type:", matrix.dtype)
print("Minimum Value:", matrix.min())
print("Maximum Value:", matrix.max())

