import numpy as np
from scipy import stats
a=np.arange(20).reshape((5,4))
print(a)
a=a.reshape((-1,1))
print(a)
print(stats.describe(a)[-1])
stats.describe(a).minmax
# ---------stats freq--------
b=["ali","huseyin","ali","ali","salah","huseyin"]
print(stats.itemfreq(b))