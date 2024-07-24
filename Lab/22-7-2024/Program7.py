# count the number of vowels and consonants in a file Myfile.txt
file = open("Myfile.txt",'w')
file.write("I love my INDIA , Ye Mera INDIA")
file.close()

file=open("India.txt",'r')
a=file.read()
b=a.lower()
o=0
for i in b:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        o+=1
print(o)
file.close()