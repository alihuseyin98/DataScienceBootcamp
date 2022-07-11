import numpy as np
# Some functions
# np.mean() returns the average
# np.sum()  returns the sum
# np.std
# np.median
# np.var()
# np.max()
# np.min()
# np.argmax()
# np.argmin()
# np.argsort()
# np.argwhere()
# np.quantile
a=np.arange(20).reshape((4,5))
print(a)
#print(a.mean())
#print(np.mean(a,axis=0))
#print(a.sum())
#print(a.std())
print(np.median(a))

print(np.sum(a, axis=0))
np.max(a, axis=0)
b=np.array([10,7,8,15,4,3])
print(b)
print(np.argmax(a,axis=1)) #Returns the indices of the maximum values along an axis.
print(np.sort(b)) # return sorted array
print(b)
print(np.argsort(b))
print(np.argwhere(b==15)[0][0])
