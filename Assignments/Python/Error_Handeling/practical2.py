# Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(f"The numbers you entered are {num1} and {num2}.")
except ValueError:
    print("Both inputs must be numerical values.")