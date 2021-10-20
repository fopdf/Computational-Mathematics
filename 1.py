import math
import numpy as np
def func_1(x,y):
    return x**2 + y**2 - 1

def func_2(x,y):
    return y - math.tan(x)

tolerance = 1e-6

F = lambda x, y: [func_1(x, y), func_2(x, y)] # матрица F
J = lambda x, y: np.array([[2*x, 2*y], [-1 / (math.cos(x)**2), 1]]) # якобиан

def NewtonMethod(A0):
    A1 = A0.copy()
    A2 = A1 - np.linalg.inv(J(*A1)) @ F(*A1)
    while abs(A2 - A1).any() > tolerance:
        A1 = A2.copy()
        A2 = A2 - np.linalg.inv(J(*A2)) @ F(*A2)
    return A2
print(NewtonMethod(np.array([1, 1])))
print(NewtonMethod(np.array([-1, -1])))