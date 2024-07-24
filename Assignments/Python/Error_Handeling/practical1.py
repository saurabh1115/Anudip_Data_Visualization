# Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(f"The numbers you entered are {num1} and {num2}.")
    div1 = num1/num2
    print(div1)
except(ZeroDivisionError):
    print("something went wrong")