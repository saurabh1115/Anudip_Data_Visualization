# Count the occurance of word "INDIA" in a text file India.txt
file = open("India.txt",'w')
file.write("I love my INDIA , Ye Mera INDIA")
file.close()

file=open("India.txt",'r')
a=file.read()
words=a.split()
o=0
for i in words:
    if(i=="INDIA"):
        o+=1
print(o)
file.close()