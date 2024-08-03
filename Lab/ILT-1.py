# 1. convert a given list into a numpy array
import numpy as np
my_list = [1,2,3,4,5]
a = np.array(my_list)
print("NumPy Array:")
print(a)
n = len(a)

# 2. display the first and the last index
print("First Index : ",my_list[0])
print("Last Index : ",my_list[n-1])
print(a*2)

# 3. write a numpy program to create an array of 10 zeros, 10 ones and 10 fives
print("array of 10 zeros")
arr1 = np.zeros((1,10))
print(arr1)

print("array of 10 ones")
arr2 = np.ones((1,10))
print(arr2)

print("array of 10 fives")