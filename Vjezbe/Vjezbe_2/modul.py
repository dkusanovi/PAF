import matplotlib.pyplot as plt
import numpy as np
import math as m

#ideja: y = 0 break :):(

def kosi_hitac(v0, theta, t, g, dt):

    theta = (theta/180)*m.pi

    x_br = 0
    y_br = 0
    t_br = 0
    x = []
    y = []
    t = []

    x.append(x_br)
    y.append(y_br)
    t.append(t_br)

    v0x = v0*(m.cos(theta))
    v0y = v0*(m.sin(theta))
    vy = v0y

    for i in range(1000):
        t_br = t_br + dt
        x_br = x_br + v0x*dt
        vy = vy - g*dt
        y_br = y_br + vy*dt
        x.append(x_br)
        y.append(y_br)
        t.append(t_br)


    for i in y:
        if i < 0:
            break




    plt.plot(x, y)
    plt.show()
    #plt.set_title("x-y graf")
    #plt.set(xlabel='put (m)', ylabel='put (m)')


kosi_hitac(50, 40, 5, 9.81, 0.01)