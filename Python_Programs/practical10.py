# Creating binary fine and accesing it
import pickle

# Write operation using dump command 
f = open("anudip.dat",'wb')
data = (10,20,30,40,50)
pickle.dump(data,f)
f.close()

# read operation using load command 
f = open("anudip.dat",'rb')
data = pickle.load(f)
print(data)
f.close()