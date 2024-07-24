# Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
try:
    num=int(input("ENTER A NUMBER: "))
except ValueError as v:
    print(v)