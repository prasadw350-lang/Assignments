# Import NumPy library
import numpy as np
# Create matrices
A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
B = np.array([[9,8,7],
              [6,5,4],
              [3,2,1]])
# Matrix Addition
print("Matrix Addition:")
print(A + B)
# Matrix Multiplication
print("\nMatrix Multiplication:")
print(A @ B)
# Element-wise Multiplication
print("\nElement-wise Multiplication:")
print(A * B)

