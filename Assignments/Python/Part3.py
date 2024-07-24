# Write a Python program to Count all letters, digits, and special symbols from the given string
Input = "P@#yn26at^&i5ve"
chars = 0
digit=0
symbols=0
for char in Input:
    if char.isalpha():
        chars+=1
    elif char.isdigit():
        digit+=1
    else:
        symbols+=1
print("Chars=",chars,"alpha=",digit,"symbols=",symbols)


# Write a Python program to remove duplicate characters of a given string
Input = "String and String Function"
result = []
words = Input.split()
for word in words:
    if word not in result:
         result.append(word)
print("String after removing duplicate words:", *result)


# Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string
Input = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
upper=0
lower=0
special=0
num=0
for char in Input:
    if char.isupper():
        upper+=1
    elif char.islower():
        lower+=1
    elif char.isnumeric():
        num+=1
    else:
        special+=1
print("UpperCase :",upper,"LowerCase :",lower,"NumberCase :",num,"SpecialCase :",special)


# Write a Python Count vowels in a string
input= "Welcome to Python Assignment"
count = 0
lower_str=input.lower()
for i in lower_str:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        count+=1
print("Total vowels are:",count)