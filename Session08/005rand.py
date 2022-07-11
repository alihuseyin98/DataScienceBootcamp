import numpy as np
np.random.seed(10)
print(np.random.rand(10))  # uniform dist.
print(np.random.randint(10,80,7))
print(np.random.randn(10))   #standard ormal dist
print(np.random.random_sample(10))
print(np.random.choice((10,100,1000,1,0),3))
print(np.random.choice((10,100,1000,1,0),3,replace=True))
print(np.random.choice((10,100,1000,1,0),3,replace=True,p=[0.96,0.01,0.01,0.01,0.01]))  