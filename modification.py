import numpy as np

# ==========================================
# 1. INSERTING ELEMENTS (np.insert)
# ==========================================
arr = np.array([10, 20, 30, 40, 50])
new_arr = np.insert(arr, 2, 99, axis=0)        # Inserting 99 at index 2
print("1D Insert:\n", new_arr)

matrix_a = np.array([[1, 2], [3, 4]])
new_matrix1 = np.insert(matrix_a, 1, [5, 6], axis=0)   # Inserting row [5, 6] at index 1
print("\n2D Insert (axis=0):\n", new_matrix1)

matrix_b = np.array([[1, 2], [3, 4]])
new_matrix2 = np.insert(matrix_b, 1, [5, 6], axis=1)   # Inserting column [5, 6] at index 1
print("\n2D Insert (axis=1):\n", new_matrix2)

matrix_c = np.array([[1, 2], [3, 4], [5, 6]])
new_matrix3 = np.insert(matrix_c, 1, [99, 100], axis=None)   # Flattened before insertion
print("\n2D Insert (axis=None):\n", new_matrix3)


# ==========================================
# 2. APPENDING ELEMENTS (np.append)
# ==========================================
arr1 = np.array([10, 20, 30, 40, 50])
new_arr1 = np.append(arr1, 60)               # Appending 60 to the end
print("\nAppend:\n", new_arr1)


# ==========================================
# 3. CONCATENATING ARRAYS (np.concatenate)
# ==========================================
arr2 = np.array([60, 70, 80, 90, 100])

# For 1D arrays, axis=0 is the only valid axis
new_arr2 = np.concatenate((arr1, arr2), axis=0)
print("\nConcatenate 1D (axis=0):\n", new_arr2)

# For 2D arrays
matrix_d = np.array([[1, 2], [3, 4]])
matrix_e = np.array([[5, 6], [7, 8]])

concat_v = np.concatenate((matrix_d, matrix_e), axis=0)
print("\nConcatenate 2D (axis=0):\n", concat_v)

concat_h = np.concatenate((matrix_d, matrix_e), axis=1)
print("\nConcatenate 2D (axis=1):\n", concat_h)

concat_flat = np.concatenate((matrix_d, matrix_e), axis=None)
print("\nConcatenate 2D (axis=None):\n", concat_flat)


# ==========================================
# 4. DELETING ELEMENTS (np.delete)
# ==========================================
arr3 = np.array([10, 20, 30, 40, 50])
new_arr5 = np.delete(arr3, 2)    # Deleting element at index 2
print("\nDelete 1D:\n", new_arr5)

# For 2D arrays
matrix_f = np.array([[1, 2], [3, 4], [5, 6]])
new_matrix4 = np.delete(matrix_f, 1, axis=0)   # Deleting row at index 1
print("\nDelete 2D (axis=0):\n", new_matrix4)

new_matrix5 = np.delete(matrix_f, 1, axis=1)   # Deleting column at index 1
print("\nDelete 2D (axis=1):\n", new_matrix5)


# ==========================================
# 5. STACKING ARRAYS (vstack, hstack, dstack)
# ==========================================
new_arr6 = np.vstack((arr1, arr2))    # Stacking vertically
print("\nVertical Stack (1D -> 2D):\n", new_arr6)

new_arr7 = np.hstack((arr1, arr2))    # Stacking horizontally
print("\nHorizontal Stack (1D -> 1D):\n", new_arr7)

# Stacking 2D matrices
new_matrix6 = np.vstack((matrix_d, matrix_e))
print("\nVertical Stack 2D:\n", new_matrix6)

new_matrix7 = np.hstack((matrix_d, matrix_e))
print("\nHorizontal Stack 2D:\n", new_matrix7)

new_matrix8 = np.dstack((matrix_d, matrix_e))
print("\nDepth Stack 2D:\n", new_matrix8)


# ==========================================
# 6. SPLITTING ARRAYS (split, vsplit, hsplit)
# ==========================================
arr4 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
new_arr8, new_arr9 = np.split(arr4, 2)    # Splitting arr4 into 2 arrays
print("\nSplit 1D:\n", new_arr8, "\n", new_arr9)

# hsplit works on 1D arrays
new_arr12, new_arr13 = np.hsplit(arr4, 2)
print("\nHorizontal Split 1D:\n", new_arr12, "\n", new_arr13)

# 2D Splitting
matrix_g = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
new_matrix9, new_matrix10 = np.split(matrix_g, 2, axis=0)    # Splitting vertically
print("\nSplit 2D (axis=0):\n", new_matrix9, "\n---\n", new_matrix10)

new_matrix11, new_matrix12 = np.split(matrix_g, 2, axis=1)    # Splitting horizontally
print("\nSplit 2D (axis=1):\n", new_matrix11, "\n---\n", new_matrix12)