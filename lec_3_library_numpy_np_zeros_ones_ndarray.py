import numpy as np
 
a = np.zeros((2, 3))
print(a)
 
a[0, 2] = 5
print(a)
 
b = np.ones((3, 2))
print(b)
 
d = np.ndarray((2, 3))
print(d)

c = np.ndarray((0, 0))
c -= 1
print(c)