# Import numpy
import numpy as np
try:
    # Take input from user
    n = int(input("How many numbers do you want to generate? "))
    # Generate random numbers
    numbers = np.random.randint(10, 101, n)
    print("\nGenerated Numbers:",numbers)
    # Statistics
    print("\nMean:", np.mean(numbers))
    print("Median:", np.median(numbers))
    print("Standard Deviation:", np.std(numbers))
    print("Minimum:", np.min(numbers))
    print("Maximum:", np.max(numbers))

    # Reshape if possible
    if n % 2 == 0:
        matrix = numbers.reshape(2, n // 2)
        print("\n2D Matrix:")
        print(matrix)
        print("\nRow-wise Sum:")
        print(np.sum(matrix, axis=1))
    else:
        print("\nCannot reshape into a 2D matrix because the number of elements"
        " is not divisible into 2 equal rows.")
except ValueError:
    print("Please enter a valid integer.")


    