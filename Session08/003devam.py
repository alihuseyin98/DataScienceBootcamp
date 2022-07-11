import numpy as np


#Return the indices of the original array that give the unique values:
a = np.array(['a', 'b', 'b', 'c', 'a'])
u, indices = np.unique(a, return_index=True)
print(u)
print(indices)
print(a[indices])
c=np.array([10,  15,  10, 15,  4,  15])
print(np.quantile(c, q=0.75))

oneyear=np.arange(np.datetime64('2000-01-01'), np.datetime64('2001-01-01'), np.timedelta64(1,'W'))
print(oneyear)
tenyar=np.arange(np.datetime64('2000'), np.datetime64('2020'), np.timedelta64(2,'Y'))
print(tenyar)
