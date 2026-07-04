# Import NumPy
import numpy as np
# Generate marks for 10 students and 5 subjects
marks = np.random.randint(30,101,(10,5))
print("Student Marks:")
print(marks)

# Total marks
total = np.sum(marks, axis=1)
# Average marks
average = np.mean(marks, axis=1)
print("\nTotal Marks:")
print(total)
print("\nAverage Marks:")
print(average)

# Highest scorer
highest = np.argmax(total)
# Lowest scorer
lowest = np.argmin(total)
print("\nHighest Scoring Student Index:", highest)
print("Marks:", marks[highest])
print("\nLowest Scoring Student Index:", lowest)
print("Marks:", marks[lowest])

# Overall class mean and sd
print("\nClass Mean:", np.mean(marks))
print("Class Standard Deviation:", np.std(marks))
# Top 3 students
top3 = np.argsort(total)[-3:]
print("\nTop 3 Students:")
print(marks[top3])
# Reshape (Demonstration)
reshaped = marks.reshape(5,10)
print("\nReshaped Array:")
print(reshaped)


