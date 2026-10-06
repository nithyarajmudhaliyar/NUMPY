import numpy as np

# ==========================================
# 1. Array Creation from Lists and Scalars
# ==========================================
l = np.array(34)
arr = np.array([1,2,3])  # Create a numpy array

print(arr)  # Print the array to the console

# The number of dimensions is decided by the number of square brackets []
# 0D = no [] e.g., np.array(34)
# 1D = 1 [] e.g., np.array([1,2,3])
# 2D = 2 [] e.g., np.array([[1,2,3],[4,5,6]])
# 3D = 3 [] e.g., np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])


# ==========================================
# 2. Array Attributes
# ==========================================
print(arr.ndim)  # Dimensions of the array (1)
print(l.ndim)    # Dimensions of the array (0)

# Shape is a tuple of number of elements in each dimension
print(arr.shape)  # Shape of the array (3,)
print(l.shape)    # Shape of the array ()


# ==========================================
# 3. Array Creation Functions
# ==========================================

# Using .arange() - (start, stop, step)
arr1 = np.arange(0,10)
print(arr1)

# Using .linspace() - (start, stop, number of values)
arr2 = np.linspace(0,5,10)
print(arr2)

# Using .logspace() - (start, stop, number of values)
arr3 = np.logspace(1,3,5)
print(arr3)

# Using .zeros() - (shape)
arr4 = np.zeros((3,4))
print(arr4)  # Maximum number of dimensions to be passed in .zeros is 32

# Using .ones() - (shape)
arr5 = np.ones((2,3,4), dtype=int)
print(arr5)  # dtype is used to specify the data type. Default is float

# Using .full() - (shape, fill_value)
arr6 = np.full((2,2),7)
print(arr6)
arr7 = np.full(10,2)
print(arr7)

# Using .empty() - (shape)
arr8 = np.empty((2,3))
print(arr8)  # Contains uninitialized (random) values, good for overwriting later


# ==========================================
# 4. Random Array Generation
# ==========================================

# Using np.random.rand() - Random values between 0 and 1
arr9 = np.random.rand(2,3)
print(arr9)

# Using np.random.randn() - Standard normal distribution (mean 0, variance 1)
arr10 = np.random.randn(2,3)
print(arr10)

# Using np.random.randint() - (start, stop, dimension)
arr11 = np.random.randint(1,100,(2,4))
print(arr11)
arr12 = np.random.randint(1,100,(2,3))
print(arr12)


# ==========================================
# 5. Special Matrices
# ==========================================

# Using np.eye() - Create an identity matrix
identity_matrix = np.eye(3)
print(identity_matrix)

# Check shape of a 2d array
arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_2d.shape)   # shape of a 2d array will print (3,3)

# Check size of array
size_arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(size_arr.size)  # size of array will print 10