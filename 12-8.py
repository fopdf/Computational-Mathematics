import math
import numpy as np

eps = 1e-3
f = lambda x: x * math.exp(-x**2) - (1 / (2 * math.sqrt(2 * math.e))) #из домашки вырзим 
h = 0.1
root = []
#Локализация корней
for x in np.arange(-2, 2, h):
    if (f(x) * f(x+h)) <= 0:
        root.append(x)
#print(root)
#Выражаем X
fi1 = lambda x: math.exp(x**2) / (2 * math.sqrt(2 * math.e))
fi2 = lambda x: math.sqrt(math.log(2 * x * math.sqrt(2 * math.e)))
def simple_iteration_method(x, fi):
    if abs(fi(x) - x) < eps / 2:
        return x
    return simple_iteration_method(fi(x), fi)
solution1 = simple_iteration_method(root[0], fi1)
solution2 = simple_iteration_method(root[1], fi2)
print(round(solution1, 3),round(solution2, 3))
print(round(abs(solution2 - solution1), 3))