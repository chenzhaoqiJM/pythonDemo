import numpy as np

import math

xcc = np.array([3,4,5]).reshape(3,1)
tcc = np.array([1,7,2]).reshape(1,3)
print(xcc.dot(tcc))

limit_f = np.array([1,2,3])
limit_f = limit_f.reshape(limit_f.shape[0],1)
limit_f_matrix = np.repeat(limit_f, 7, axis=1)
print(limit_f_matrix)
print(limit_f_matrix.shape)


cvv = np.array([[3,5,7],[3,2,9],[7,1,4]])
print(cvv.sum(axis=1))