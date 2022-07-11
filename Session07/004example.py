from turtle import right, shape
import numpy as np



arr=np.loadtxt(r'D:\Documents\Codes\answers.txt',delimiter=",",dtype=str)
print( arr[:,0][arr[:,1]=="A"],arr[:,1][arr[:,1]=="A"])
print( arr[arr==""])

arr2=np.zeros((10,10)) 

#arr2[:,0]=1
#arr2[:,-1]=1
arr2[:,[0,-1]]=1
#arr2[0,:]=1
#arr2[-1:,:]=1
#arr2[[0,-1],:]=1
print(arr2)
print(np.ones((10,10))*6)
#---------------
arr3=np.arange(5)
arr3[0]=5.2 # edit it as int 
print(arr3)
arr3=arr3.astype(float)
arr3[0]=5.2 
print(arr3)
