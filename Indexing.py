import numpy as np

# ==========================================
# ==========================================
# 1. Fancy Indexing - pass indexes as list to fetch them in the order of the list
# ==========================================
arr = np.array([1,2,3,4,5])
print(arr[[2,0,1]])     # 3,1,2

# ==========================================
# 2. Boolean Masking - Used to select elements based on a condition
# ==========================================
mask = arr > 2   # mask is a boolean array
print(mask)     # [False, False, True, True, True]
print(arr[mask])    # [3,4,5]
