from lec_3_task_1 import k, e, h
from math import *
T = 200
E = 300
N = (2 / (sqrt(pi))) * (h /((k * T) * (3 / 2))) * (e ** (-E / (k * T))) * (E ** (T / 2))
print(N)