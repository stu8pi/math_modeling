from lec_3_task_1 import g
import numpy as np
v0 = float(input())
x0 = float(input())
y0 = float(input())
for t in range(6):
    x = x0 + (v0 * t)
    y = y0 + (v0 * t) - ((g * t ** 2) / 2)
    print(t, np.array(x), np.array(y))