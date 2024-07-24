# count and display the number of words starting with "T" in a file Word.txt
file = open("Word.txt","w")
file.write("The quick brown fox jumps over the lazy dog. \n")
file.write("INDIA is a diverse country with rich cultural heritage.\n")
file.write("Technology is advancing at an unprecedented pace.\n")
file.write("Hello saurabh, welcome to the python class.\n")
file.write("Tomorrow, we will explore more advanced topics.\n")
file.write("Taking small steps every day leads to big achievements.\n")
file.close()

file = open("Story.txt","r")
lines = file.read()
b = lines.split()
count = 0
for x in b:
    if x.startswith("T"):
        count += 1
        print(x)
print(f"Total lines starting with 'T': {count}")