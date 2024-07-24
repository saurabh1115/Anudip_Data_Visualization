# Write a Python program to count the occurrences of each word in a given sentence
str = "To change the overall look of your document. To change the look available in the gallery"
str.lower()
words = str.split()
word_count={}
for word in words:
    if word in word_count:
       word_count[word]+=1
    else:
       word_count[word]=1
print(word_count)


# Write a Python program to remove a newline in Python
str = "\nBest \nDeeptech \nPython \nTraining\n"    
print(str.replace("\n",""))


# Write a Python program to reverse words in a string 
str="Deeptech Python Training"
print(str[::-1])


# Write a Python program to count and display the vowels of a given text
str = "Welcome to python Training"
count = 0
lower_str=str.lower()
for i in lower_str:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        count+=1
        print(i,count)