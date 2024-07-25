# Exception handeling
print("Line 1")
print("Line 2")
print("Line 3")
print("Line 4")
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
try:
    print(num1/num2)
    open("anudip.txt")
# this runs if exception occurs
except(ZeroDivisionError,FileNotFoundError):
    print("something went wrong")

# this runs if exception does not occur
else:
    print("else block")
    
# this runs either exception occurs or not
finally:
    print("finally block")
    
print("Line 6")