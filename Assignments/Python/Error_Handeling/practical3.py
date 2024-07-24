# Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
try:
    open("anudip.txt")
except(FileNotFoundError):
    print("the file does not exist")