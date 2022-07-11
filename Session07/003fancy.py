from turtle import right, shape
import numpy as np

x=np.array([1,2,3,4,5])

mask=np.array([True, True, False, False, False])
mask1=np.array([1,1,1,1,0])
mask2=np.array([1,4,3,2,2])
print(x>3)                                          #[False False False  True  True]
print(x[x<3])                                       #[1 2]
print(x[mask])                                      #[1 2]
print(x[mask1])
print("+-+-",x[x==mask2])
#--------------------------------
a1=np.array([1,2,3,4,5,6])
a2=np.array([0,20,30,4,5,6])
print("a1[a1<a2] ",a1[a1<a2])

