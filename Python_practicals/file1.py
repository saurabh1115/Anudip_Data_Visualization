# creates a file if it does not exist and rewrites the file if it already exists (Write Mode)
file = open("anudip.txt",'w')
file.write("Welcome to Python Class \n")
file.close()

# creates a file if it does not exist and starts the pointer from the end of the existing file
file = open("anudip.txt",'a')
file.write("My name is Saurabh Negi")
file.close()

# tell is used to retreive the position of the cursor
#print(file.tell())

# seek is used to move the position of the cursor
#file.seek(12)
