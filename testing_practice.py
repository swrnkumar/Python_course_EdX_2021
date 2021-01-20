# solving matrices using numpy

import numpy as np
import scipy

a = np.array([[3,1], [1,2]])
b = np.array([9,8])
x = np.linalg.solve(a, b)
x
array([2.,  3.])

print (array)