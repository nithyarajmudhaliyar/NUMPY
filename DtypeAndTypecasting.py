import numpy as np  

# arr = np.array([1,2,3.1])    # if instead of 3.1 we put 3 numbers would be of int type and if '3' then of string type
# print(arr)
# print(type(arr))

# lst = [1,2,3,4,5]
# print(type(lst))
# arr1 = np.array(lst)
# print(arr1)
# print(type(arr1))
# print(arr1.dtype)

# Data type     Description        Example values
# int32       32-Bit Integers     -1, 0, 1, 2, 3
# int64       64-Bit Integers     100 , 1000, -250
# float32     Floating point      -1.0, 0.0, 1.5, 2.7
# float64     Floating point      -1.00000001
# complex     Complex numbers     1+2j, 3+4j
# bool        Boolean values      True, False
# str         String values       'Hello', 'NumPy'

l =np.array([1,2,3],dtype="S")   # S is for string
print(l)
print(l.dtype)

l =np.array([1,2,3],dtype="i4")   # i4 is for 4 byte integer
print(l)
print(l.dtype)

l =np.array([1,2,3],dtype="f")   # f is for float
print(l)
print(l.dtype)

# Type casting
arr = np.array([1,2,3,4])
print(arr.dtype)    
arr = arr.astype('float32')      # cast the array to float32
print(arr)
print(arr.dtype)