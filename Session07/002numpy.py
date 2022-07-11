from turtle import right, shape
import numpy as np
L=[9,4,5,7,8,9]                 # all data has the same data type
#                               #L=9,[4,5,7,8,9]  -> [9 list([4, 5, 7, 8, 9])]
a=np.array(L)                   # creat an array
print(a)
print(a.dtype)                  #    <U32 / float64 / int32
a=np.ones((2,5,10,4))               #np.zeros() (rowa,columns)
b=np.ones((5,3))  
print(b)
#--------------------------
np.array([[1,2,3],[4,5,6]])
#------------arange--------
c=np.array(list(range(10)))
print(c)
d=np.arange(1.5,12)             # float accepted as range
d=np.arange(3,12,dtype=float)  
print(d)
#------------linspace--------
e=np.linspace(2,12,7)
print("E \n",e)
#------------eye------------
f=np.eye(4)                   #np.eye(4,5)
print(f)
print("---",b.shape)
#---------shape an array is (mutable)------- occure error 
g=np.arange(32)  
print(g)
g.shape=(4,8) # 4*8 = 32
print(g)
g.shape=(8,4)
print(g)
#---------reshape an array is (unmutable)------- occure error   object attribute 'reshape' is read-only
# return a value not change it
print("-----------------------\n")
g=np.arange(32)  
print(g)
g.reshape(4,8) # 4*8 = 32 
print(g)
print(g.reshape(8,4))
print(g)

# Operations---------------------
h=np.arange(10)
i= np.arange(10,20)
print("   ",h)
print("   ",i)
print(" + ",h+i)
print(" - ",h-i)
print(" * ",h*i)
print(" / ",h/i)
print(" % ",h%i)
print(" ** ",h**i)
print(" & ",h&i)
print(" | ",h|i)
# + - * / % **
# Comparison
# > < >= <= == !=
# Logical
# &, |, ~ for arrays contain true false vcalue
# Broadcasting
# + - * / % **
# .all, any
h=np.array([1,0,0])
print((h>-1).all(0))
print(h.all(0))
print((h).any(0))
"""a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
c = np.array([1,2,3,4])

print((a == b ).all())  #False
print((a == c ).all())   # True
print((a == b ).any())   #False
print((a == c ).any())   #True
print((a > 3 ).all())    #False"""