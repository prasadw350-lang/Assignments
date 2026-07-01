# Import NumPy 
import numpy as np
array = np.random.randint(1, 51, 20)
print("1D Array:")
print(array)

# Reshape into 4x5 matrix
matrix = array.reshape(4,5)
print("\n4x5 Matrix:")
print(matrix)

# sum, mean, and standard deviation of matrix
print("\nSum:", np.sum(matrix))
print("Mean:", np.mean(matrix))
print("Standard Deviation:", np.std(matrix))

# Maximum value in each row
print("\nMaximum Value in Each Row:")
print(np.max(matrix, axis=1))

