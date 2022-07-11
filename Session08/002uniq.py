import numpy as np


c=np.array([10,  15,  10, 15,  4,  15])
print(np.unique(c))
print(np.unique(c,return_counts=True))
# axiss unique ---------
a = np.array([[1, 0, 0], [1, 0, 0], [2, 3, 4]]) #?
print(np.unique(a, axis=1,return_counts=True)) 
d=np.arange(12).reshape(3,4)
#print(d)
#print(d[:,0])