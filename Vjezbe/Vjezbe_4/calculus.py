import matplotlib.pyplot as plt
import numpy as np 


def f(x):
    return x**3+2*x + 3

def a_f(x):
    return 3*x**2+2


def g(x):
    return np.sin(x) + 4

def a_g(x):
    return np.cos(x)


def fun(x):
    return 2*x**2 + 3
    
def i_fun(x):
    return (2/3)*x*3 + 3*x




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

    return x, dfx


def integrate(f, d, g, n):
    dx = (g-d)/n
    sum_d_br = 0
    sum_g_br = 0

    for i in range(n):
        sum_d_br = sum_d_br + f(d + i*dx)*dx
        sum_g_br = sum_g_br + f(d + (i+1)*dx)*dx
    return sum_d_br, sum_g_br


def trapez(f, d, g, n):
    dx = (g-d)/n
    br = 0.5 * (f(d) + f(g))*dx

    for i in range(1, int(n)):
        br = br + dx * f(i * dx)
    return br