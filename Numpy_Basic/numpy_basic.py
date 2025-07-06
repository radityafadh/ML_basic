import numpy as np

# Create 1D arrays
a = np.array([1, 2, 3])  # array a = [1, 2, 3]
b = np.array([4, 5, 6])  # array b = [4, 5, 6]

# Overwriting 'a' with a 2D array (2 rows, 3 columns)
a = np.array([[1, 2, 3], [4, 5, 6]])

# Display arrays
print("This is array a = ", a)
print("This is array b = ", b)

# Create a 1D array with numbers from 0 to 999
c = np.arange(1000)

# Create a 2D array with values from 0 to 11, shaped as (3 rows x 4 columns)
d = np.arange(12).reshape(3, 4)
print("This is array d = \n", d)

# === Array Slicing ===
# d[0:2, 1:2] selects rows 0 and 1, and column 1 only (result is 2x1 matrix)
print("This is d[0:2, 1:2]= ", d[0:2, 1:2])

# d[0:2, 0:3] selects rows 0 and 1, and columns 0 to 2 (not including 3)
print("This is d[0:2, 2:2] = ", d[0:2, 0:3])  # note: comment label misleading; should be [0:2, 0:3]

# Get a single element from row 1, column 2 (zero-based indexing)
print("This is the element at d[1, 2] = ", d[1, 2])

# === Summary Statistics ===
# Calculate and display common statistics on array d
print("This is the sum of d = ", d.sum())         # Sum of all elements
print("This is the mean of d = ", d.mean())       # Mean (average) of all elements
print("This is the max of d = ", d.max())         # Maximum value
print("This is the min of d = ", d.min())         # Minimum value
print("This is the std of d = ", d.std())         # Standard deviation

# === Broadcasting and Vectorization ===
# Add 10 to every element in array d
print("all the array is increased by 10 = \n", d + 10)

# Multiply every element by 10
print("all the array is multiplied by 10 = \n", d * 10)

# === Boolean Masking ===
print("you use d>=5 to make the true or false, and add [] to case the index")

# Create a boolean array where condition d >= 5 is checked element-wise
print("make the boolean of array that's more than equal to 5 = \n", d >= 5)

# Get all elements in d that are greater than or equal to 5
print("find the index of array that's more than equal to 5 = \n", d[d >= 5])

# Get all elements in d that are greater than the mean of d
print("find the index of array that's bigger than mean = \n", d[d > d.mean()])

# Combine two conditions:
# (1) d > 2 OR (2) d % 2 == 0 (i.e., even numbers)
print("find the index that is bigger than 2 or is modulo 2 == 0 = \n", d[(d > 2) | (d % 2 == 0)])

# === Linear Algebra Operations ===
print("transpose, cross, dot product")

# Transpose of array d (rows become columns)
print("d.T = \n", d.T)

# Dot product of d and its transpose (d • dᵀ)
print("d.dot(d.T) = \n", d.dot(d.T))

# Equivalent to above: transpose of d, then dot product with original
print("d.transpose().dot(d) = \n", d.transpose().dot(d))

# Equivalent syntax using '@' operator for matrix multiplication
print("d @ d.T = \n", d @ d.T)
