# display the lines having more than 5 words in a text file Notes.txt
file = open("Notes.txt","w")
file.write("The quick brown fox jumps over the lazy dog. \n")
file.write("INDIA is a diverse country with rich cultural heritage.\n")
file.write("Technology is advancing at an unprecedented pace.\n")
file.write("Hello saurabh.\n")
file.write("welcome to the python class.\n")
file.write("Tomorrow, we will explore more advanced topics.\n")
file.write("Taking small steps every day leads to big achievements.\n")
file.close()

file = open("Notes.txt", 'r')
for line in file:
    words = line.split()
    if len(words) > 5:
        print(line)