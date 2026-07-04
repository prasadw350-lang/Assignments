# Import NumPy
import numpy as np
# Create matrices
A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
B = np.array([[9,8,7],
              [6,5,4],
              [3,2,1]])
# Element-wise Multiplication
print("Element-wise Multiplication:")
print(A * B)
# Matrix Multiplication
print("\nMatrix Multiplication:")
print(A @ B)
# Difference:
# *  -> Multiplies corresponding elements.
# @  -> Performs matrix multiplication (row × column)

