import math
import numpy as np

eps = 1e-3

f = lambda x: math.exp(x) - 3*x**2 - 1  #f(x) - f'(0)

h = 0.1
root = []
#Локализация корней
for x in np.arange(-2, 2, h):
    if (f(x) * f(x+h)) <= 0:
        root.append(x)
print(root)

#Выражаем X
fi1 = lambda x: (math.exp(x) / (3*x))
fi2 = lambda x: (3 * math.log(math.sqrt(3)*x) - (x/2))

def simple_iteration_method(x, fi, i):
    i = i + 1
    if abs(fi(x) - x) < eps / 2:
        return x, i
    return simple_iteration_method(fi(x), fi, i)

solution1 = simple_iteration_method(root[1], fi1,0)

#solution2 = simple_iteration_method(root[1], fi2,0)  |(fi2)'| > 1 метод расходится и не подходит |3/x - 1/2| на нашем отрезке больше 1.
print(solution1)
