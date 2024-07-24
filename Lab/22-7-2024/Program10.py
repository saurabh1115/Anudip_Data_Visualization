# create a binary file "Stu.dat" and enter Student name, roll no. and marks till the user wants
import csv

# writing students data in the file 
file = open("Stu.dat",'a',newline='')
wo = csv.writer(file)
data = [["a","b","c","d"],[1,2,3,4],[60,80,70,65]]
wo.writerows(data)
file.close

# reading students data from the file
file = open("Stu.dat",'r')
re = csv.reader(file)
list = list(re)
for x in list:
    print(x)
file.close