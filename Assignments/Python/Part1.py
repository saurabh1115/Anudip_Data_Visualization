import random

# Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.
def div(a,b):
    result =a/b
    print(result)
div(20,10)


# Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number 
def square(a):
    result= a*a
    print(result)
square(5)


# Using max() and min() functions display the maximum and minimum of 5 random numbers.
random_numbers = [random.randint(1, 100) for _ in range(5)]
print("Random Numbers:", random_numbers)
max_number = max(random_numbers)
min_number = min(random_numbers)
print("The maximum number is:", max_number)
print("The minimum number is:", min_number)


# Accept a name from the user and display that in lower case using lower() function
name = input("Enter You Name: ")
print("Name in Lower Case: ",name.lower())