# saving data as binary
import pickle
f=open('data2.dat','wb')
pickle.dump([6,2,4,5], f)
f.close()
# read data from binary file
import pickle
f=open('data2.dat','rb')
L2=pickle.load(f)
print(sorted(L2))