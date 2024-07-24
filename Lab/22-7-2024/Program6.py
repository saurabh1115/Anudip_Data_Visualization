# Count and display the lines starting with "T" in a text file Story.txt
file = open("Story.txt","w")
file.write("The quick brown fox jumps over the lazy dog. \n")
file.write("INDIA is a diverse country with rich cultural heritage.\n")
file.write("Technology is advancing at an unprecedented pace.\n")
file.write("Hello sarthak, welcome to the python class.\n")
file.write("Tomorrow, we will explore more advanced topics.\n")
file.write("Taking small steps every day leads to big achievements.\n")
file.close()

file = open("Story.txt","r")
lines = file.readlines()
count = 0
for line in lines:
    if line.strip().startswith("T"):
        count += 1
        print(line.strip())
print(f"Total lines starting with 'T': {count}")
file.close()