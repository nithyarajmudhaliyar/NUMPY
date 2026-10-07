import numpy as np

# ==========================================
# 1. Handling Missing Values (NaN)
# ==========================================
arr = np.array([1, 2, 3, np.nan, 5, np.nan])

# np.isnan() returns a boolean array where True indicates a NaN value
print("Check for NaN values (np.isnan):")
print(np.isnan(arr))

# Note: You cannot compare NaN with NaN using standard equality.
# print(np.nan == np.nan)  # This will evaluate to False

# np.nan_to_num(array, nan=value) replaces NaN with the specified value (default is 0)
cleaned_arr = np.nan_to_num(arr, nan=0)
print("\nArray after replacing NaN with 0:")
print(cleaned_arr)


# ==========================================
# 2. Handling Infinite Values (Inf)
# ==========================================
arr2 = np.array([1, 2, 3, np.inf, 5, -np.inf])

# np.isinf() returns a boolean array where True indicates an infinite value
print("\nCheck for infinite values (np.isinf):")
print(np.isinf(arr2))

# np.nan_to_num() can also replace positive and negative infinity
cleaned_arr2 = np.nan_to_num(arr2, posinf=1000, neginf=-1000)
print("\nArray after replacing Inf with 1000 and -Inf with -1000:")
print(cleaned_arr2)
