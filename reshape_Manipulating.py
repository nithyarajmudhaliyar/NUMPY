import numpy as np

# ==========================================
# 1. Reshaping Arrays
# ==========================================
# Reshape is used to change the dimension of an array without changing its data.
arr = np.array([1,2,3,4,5,6,7,8,9,10])

# reshape(rows, columns) - specifies new shape if dimensions match
reshaped_arr1 = arr.reshape(5,2)      
print(reshaped_arr1)

# Error Example:
# The number of elements in the array must match the reshaped dimensions.
# arr2 = np.array([1,2,3,4,5,6,7,8,9])
# reshaped_arr2 = arr2.reshape(2, 5)  # Raises ValueError: cannot reshape array of size 9 into shape (2,5)


# ==========================================
# 2. Reshaping Returns a View, Not a Copy
# ==========================================
# Reshaping does not create a copy; it returns a view of the original array.
original = np.array([1,2,3,4])

# Create a reshaped view
reshaped = original.reshape(2,2)

# Modify the first element of the reshaped array
reshaped[0,0] = 99

# Check the original array to see the modification
print(original)  # Output: [99  2  3  4]


# ==========================================
# 3. Flattening the Array
# ==========================================
matrix_a = np.array([[1,2,3],[4,5,6]])

# .ravel() - Returns a flattened 1D array (a view of the original)
print(matrix_a.ravel())

# .flatten() - Returns a flattened 1D array (a copy of the original)
print(matrix_a.flatten())