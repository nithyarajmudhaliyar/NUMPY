import numpy as np

# ==========================================
# 1. Vectorization vs Normal Loop
# ==========================================
# Vectorization is performing operations on arrays of the same shapes without explicit loops.

# Normal way (using lists and loops)
arr_list = [100, 200, 300]
discount = 10      # 10% discount
finalPrice_list = []
for i in arr_list:
    finalPrice_list.append(i - (i * discount / 100))
print("Normal way result:\n", finalPrice_list)

# NumPy way (Vectorization)
arr_np = np.array([100, 200, 300])
discount_np = 10   # 10% discount
finalPrice_np = arr_np - (arr_np * discount_np / 100)
print("\nNumPy way result:\n", finalPrice_np)


# ==========================================
# 2. Broadcasting
# ==========================================
# Broadcasting allows NumPy to perform operations on arrays of different shapes.

# Expanding single elements (Scalar Broadcasting)
# [1, 2, 3] + 10 = [11, 12, 13]
scalar_add = np.array([1, 2, 3]) + 10
print("\nScalar Broadcasting ([1, 2, 3] + 10):\n", scalar_add)

# Matching Dimensions (Vector + Matrix)
# [1, 2, 3] + [[1, 2, 3], [4, 5, 6]] = [[2, 4, 6], [5, 7, 9]]
vector = np.array([1, 2, 3])
matrix = np.array([[1, 2, 3], [4, 5, 6]])
matrix_add = vector + matrix
print("\nVector + Matrix Broadcasting:\n", matrix_add)

# Incompatible shapes - [1, 2, 3] + [1, 2] --> Raises ValueError
# try:
#     incompatible = np.array([1, 2, 3]) + np.array([1, 2])
# except ValueError as e:
#     print("\nIncompatible shapes error:\n", e)