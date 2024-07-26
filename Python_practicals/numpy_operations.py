# numpy operations
import numpy as np

# creation of arrays
a=np.array(42)
b=np.array([1,2,2,3,4])
c= np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
d=np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print("a array",a)
print("b array",b)
print("c array",c)
print("d array",d)

# using .ndim to get the dimensions of array 
print("a array dime",a.ndim)
print("b array dime",b.ndim)
print("c array dime",c.ndim)
print("d array dime",d.ndim)

# slicing
arr=np.array([1,2,3,4,5,6,7,8])
sarr = arr[1:5]
print(arr)
print(sarr)
sarr[2]=100   # Changing value in copy array will also be reflected in origial Array i.e it is just a view of original array.
print(arr)
print(sarr)

# copy function,The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.
arr=np.array([1,2,3,4,5])
arr2=arr.copy()
arr[0]=42
print(arr)
print(arr2)

# view function,The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.
arr=np.array([1,2,3,4,5])
arr2=arr.view()
arr[0]=42
print(arr)
print(arr2)

# The numpy.zeros() function is one of the most significant functions which is used in machine learning programs widely. This function is used to generate an array containing zeros.The numpy.zeros() function provide a new array of given shape and type, which is filled with zeros.
a=np.zeros((6,3))
print(a)

# The NumPy ones() function in Python is used to create an array of the specified shape and type, where all the elements are set to 1. This function is very similar to zeros(). The ones () function takes three arguments and returns the array filled with value 1. In this article, I will explain how to use the NumPy ones() function with examples.
a=np.ones((6,3))*9 # it multiply with ones at the diagonal
print(a)

# The eye tool returns a 2-D array with 1's as the diagonal and 0's elsewhere. The diagonal can be main, upper, or lower depending on the optional parameter k. A positive k is for the upper diagonal, a negative k is for the lower, and a Øk (default) is for the main diagonal.
a=np.eye(4)
print(a)

# The diag tool returns a 2D array with input numbers as the diagonal and 0's elsewhere.
a=np.diag((3,4,5,6))
print(a)

# the diag tool returns the diagonal values of the 2D array
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.diag(arr))

# randint() is used to generate random integers
rand = np.random.randint(0,10,2)
print(rand)

# reshape function helps us to change the dimension of an array without changing its data
arr = np.random.randint(0,100,12)
print(arr)
arr = arr.reshape(4,3)
print(arr)
print("Array value is ", arr[0][1])
print("Array value is ", arr[1][0])
print(arr.shape)
arr = arr.reshape(-1,4)
print(arr)
arr = arr.reshape(2,-1)
print(arr)

# seed is used to generate the same random value 
np.random.seed(145)
arr = np.random.randint(0,100,12)
print(arr)

# slicing
arr = np.array([[1,2,3,4,5],[4,5,6,7,8],[7,8,9,10,11],[9,10,11,12,13],[11,12,13,14,15],[13,14,15,16,17]])
print(arr[2:,2:])
print(arr[3:5,2:4])

# arange is used to generate values in order
arr = np.arange(1,11)
print(arr)
print(arr[arr%2==0]) # gives even numbers
print(arr[arr%2!=0]) # gives odd number
arr[arr%2==0] = 0 # 
print(arr)
arr = np.arange(1,8)
print(arr+2)
print(arr*2)
print(arr**2)

# mathematical functions
arr = np.array([10,20,30,25,6,2])
print(np.min(arr))
print(np.max(arr))
print(np.argmin(arr))
print(np.argmax(arr))
print(np.sqrt(arr))
print(np.sin(arr))
print(np.cos(arr))

# Seed the random number generator
np.random.seed(122)

# Generate a random array of integers between 1 and 20 with a total of 9 elements, and reshape it to a 3x3 matrix
mat = np.random.randint(1, 21, 9).reshape(3, 3)

# Print the matrix
print("Matrix:\n", mat)

# Print the sum of all elements in the matrix
print("Sum of all elements:", np.sum(mat))

# Print the cumulative sum of elements in the matrix
print("Cumulative sum of all elements:\n", np.cumsum(mat))

# Print the minimum value in the matrix
print("Minimum value in the matrix:", np.min(mat))

# Print the maximum value in the matrix
print("Maximum value in the matrix:", np.max(mat))

print("\n--\n")

# Print the sum of elements along each row
print("Sum of elements along each row:", np.sum(mat, axis=1))

# Print the minimum value in each row
print("Minimum value in each row:", np.min(mat, axis=1))

# Print the maximum value in each row
print("Maximum value in each row:", np.max(mat, axis=1))

# Print the cumulative sum of elements along each row
print("Cumulative sum along each row:\n", np.cumsum(mat,axis=1))

np.random.seed(122)
mat = np.random.randint(1, 21, 9)
print(mat)
np.random.shuffle(mat)
print(mat)
print(np.unique(mat,return_index=True,return_counts=True))
print(np.unique(mat).size)