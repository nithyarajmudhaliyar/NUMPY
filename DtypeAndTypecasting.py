import numpy as np

# ==========================================
# 1. Implicit Data Typing
# ==========================================
# If we mix types (e.g., ints and floats), NumPy upcasts to the most general type.
# For example, 3.1 makes the array float type, '3' would make it string type.
arr = np.array([1,2,3.1])
print(arr)
print(type(arr))


# ==========================================
# 2. Conversion from Python Lists
# ==========================================
lst = [1,2,3,4,5]
print(type(lst))

arr1 = np.array(lst)
print(arr1)
print(type(arr1))
print(arr1.dtype)


# ==========================================
# 3. Common NumPy Data Types Reference
# ==========================================
# Data type     Description        Example values
# int32       32-Bit Integers     -1, 0, 1, 2, 3
# int64       64-Bit Integers     100, 1000, -250
# float32     Floating point      -1.0, 0.0, 1.5, 2.7
# float64     Floating point      -1.00000001
# complex     Complex numbers     1+2j, 3+4j
# bool        Boolean values      True, False
# str         String values       'Hello', 'NumPy'


# ==========================================
# 4. Explicit Data Typing (using dtype)
# ==========================================

# 'S' or 'S' followed by length for string
l_str = np.array([1,2,3],dtype="S")
print(l_str)
print(l_str.dtype)

# 'i4' for 4-byte (32-bit) integer
l_int = np.array([1,2,3],dtype="i4")
print(l_int)
print(l_int.dtype)

# 'f' for float
l_float = np.array([1,2,3],dtype="f")
print(l_float)
print(l_float.dtype)


# ==========================================
# 5. Type Casting (using astype)
# ==========================================
arr_cast = np.array([1,2,3,4])
print("Original dtype:",arr_cast.dtype)

# Cast the array to float32
arr_cast = arr_cast.astype('float32')
print(arr_cast)
print("New dtype:",arr_cast.dtype)