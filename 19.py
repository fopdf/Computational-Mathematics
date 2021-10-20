from sympy import diff, symbols, sin, exp, lambdify, factorial
import matplotlib.pyplot as plt

def func1():
    t = symbols('t')
    y = sin(t)
    return y

def func2():
    t = symbols('t')
    y = exp(t)
    return y

def Maclaurin_row(n,u):
    t = symbols('t')
    u1 = lambdify(t,u)
    
    if (n == 0):
    
        return u1(0)
    
    else:
        sum = u1(0)
        temp = u
        i = 1
        while i < n:
            temp = diff(temp,t)
            product = lambdify(t,temp)
            sum = sum + (product(0) * (t**i))/factorial(i)
            i += 1
    
    return sum        


print('sin(t):', Maclaurin_row(5,func1()))
print('exp(t):', Maclaurin_row(5,func2()))

