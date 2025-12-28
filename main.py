import numpy as np   # as np is a alias for numpy
l = np.array(34) 
arr = np.array([1,2,3])  # Create a numpy array and assign it to a variable named arr
print(arr.ndim)  # Print the a dimensions of the array using the .ndim attribute which is 1
print(l.ndim)   # Print the a dimensions of the array using the .ndim attribute which is 0
print(arr)  # Print the array to the console
# the number of dimensions is decided by []
# 0D = no [] e.g. np.array(34)
# 1D = 1 [] e.g. np.array([1,2,3])
# 2D = 2 [] e.g. np.array([[1,2,3],[4,5,6]])
# 3D = 3 [] e.g. np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr.shape)  # Print the shape of the array using the .shape attribute which is (3,)
# shape is a tuple of number of elements in each dimension
print(l.shape)  # Print the shape of the array using the .shape attribute which is ()

#easier way to create a list using .arange() function
arr1 = np.arange(0,10)    #(start , stop , step)     # Create an array with values ranging from 0 to 9 using the np.arange() function and assign it to a variable named arr1
print(arr1)

# using linspace to create an array
arr2 = np.linspace(0,5,10)   #(start , stop , number of values)   # Create an array with 10 values evenly spaced between 0 and 5 using the .linspace()
print(arr2)

# using logspace to create an array
arr3 = np.logspace(1,3,5)   #(start , stop , number of values)   # Create an array with 5 values evenly spaced on a log scale between 10^1 and 10^3 using the .logspace()
print(arr3)

# using zeros to create an array
arr4 = np.zeros((3,4))   #(shape)   # Create a 3x4 array filled with zeros using the .zeros() function
print(arr4)        # maximum number of dimensions to be passed in .zeros is 32

# using ones to create an array
arr5 = np.ones((2,3,4), dtype=int)   #(shape)   # Create a 2x3x4 array filled with ones using the .ones() function
print(arr5)       # dtype is used to specify the data type of the array elements  if not specified default is float

# using full to create an array
arr6 = np.full((2,2), 7)   #(shape , fill value)   # Create a 2x2 array filled with the value 7 using the .full() function
print(arr6)
arr7 = np.full(10,2)
print(arr7)

# using empty to create an array
arr8 = np.empty((2,3))   #(shape)   # Create a 2x3 array without initializing its values using the .empty() function
print(arr8)    # note it is not filled with zeros it contains random values and it's good if you want to overwrite all the values later

# using np.random.rand()
arr8 = np.random.rand(2,3)    # create a 2x3 array with random values between 0 and 1
print(arr8)

# using np.random.randn()
arr9 = np.random.randn(2,3)    # create a 2x3 array with random values from a standard normal distribution mean 0 and standard deviation 1
print(arr9)

# using np.random.randint()
arr10 = np.random.randint(1,100,(2,3))   # (start , stop , dimension)   # create a 2x3 array with random integer values between 1 and 9
print(arr10)