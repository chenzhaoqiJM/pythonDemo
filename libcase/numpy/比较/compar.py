import numpy as np

#比较操作
a= np.array([[1,3,7],[8,11,65]])

#Return self< value.
b_lt = a.__lt__(3)
print(b_lt,'\n')

#Return self<=value.
b_le = a.__le__(3)
print(b_le)


#__gt__ Return self>value.
#__ge__ Return self>=value.
#__eq__ Return self==value.
#__ne__ Return self!=value.


#ndarray.__neg__(/) -self

b_neg = a.__neg__()
print(b_neg)

