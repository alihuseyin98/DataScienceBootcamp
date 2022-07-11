from turtle import right, shape
import numpy as np

b=np.arange(12).reshape(3,4)
print(b)
print(b[1:,1])  # direct access
print(b[1:][1])
print(b[1:][1][1])