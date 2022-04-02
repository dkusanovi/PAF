from cmath import tan
import matplotlib.pyplot as plt
import numpy as np 

def f(x):
    return x**3+2*x

def dora(x):
    return 5*x**3 - 2*x**2 + 2*x - 3

def g(x):
    return tan(x)

def two_point(f, x, h):
    return (f(x+h)-f(x))/h

def three_point(f, x, h):
    return (f(x+h)-f(x-h))/(2*h)




def raspon(f, g, d, h, m = 3):
    br_koraka = int(1/h)
    x = np.linspace(g, d, br_koraka)
    dfx = []

    if m == 2:
        for el in x:
            rez = two_point(f, el, h)
            dfx.append(rez)
    elif m == 3:
        for el in x:
            rez = three_point(f, el, h)
            dfx.append(rez)

    plt.plot(x, dfx)
    plt.show()

    return x, dfx


def integrate(f, d, g, n):
    dx = (g-d)/n
    sum_d = 0
    sum_g = 0

    for i in range(n):
        sum_d = sum_d + f(d + i*dx)*dx
        sum_g = sum_g + f(d + (i+1)*dx)*dx
    return sum_d, sum_g

rez1, rez2 = integrate(f, 0, 1, 100)


def trapez(f, n, d, g):
    dx = (g-d)/n
    br = 0.5 * (f(d) + f(g))*dx
    for i in range(1, int(n)):
        br = br + dx * f(i * dx)
    return br
 
# print(trapez(f, 100, 0, 1))

raspon(dora, -2, 2, 0.01)


