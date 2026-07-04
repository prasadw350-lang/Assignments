import numpy as np
# Create a 4x5 matrix with random integers between 20 and 80
matrix = np.random.randint(20, 81, (4, 5))
print("Matrix:")
print(matrix)

# Statistics
print("\nMinimum Value:", np.min(matrix))
print("Maximum Value:", np.max(matrix))
print("Sum:", np.sum(matrix))
print("Mean:", np.mean(matrix))
print("Standard Deviation:", np.std(matrix))

# Row-wise sum
print("\nRow-wise Sum:")
print(np.sum(matrix, axis=1))
# Column-wise sum
print("\nColumn-wise Sum:")
print(np.sum(matrix, axis=0))