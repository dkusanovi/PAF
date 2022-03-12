import matplotlib.pyplot as plt
import numpy as np
import math as m


def jednoliko_gibanje(F, m, t, deltat):

    x = []
    v = []
    a = []
    t = []

    x_br = 0
    v_br = 0
    t_br = 0
    akc = F/m

    x.append(x_br)
    v.append(v_br)
    t.append(t_br)
    a.append(akc)

    # for po delta t
    # t = i*deltat

    for i in range(1000):
        t_br = t_br + deltat
        v_br = v_br + akc*deltat  
        x_br = x_br + v_br*deltat 
        # i = i + 1
        # x.append(x[i] + v[i]*deltat)
        # v.append(v[i] + a*deltat)
        # a.append(akc)
        # t.append(i*deltat)
        x.append(x_br)
        v.append(v_br)
        a.append(akc)
        t.append(t_br)


    fig, axs = plt.subplots(1, 3, figsize=(14, 4))
    axs[0].plot(t, x)
    axs[0].set_title("x-t graf")
    axs[0].set(xlabel='vrijeme (s)', ylabel='put (m)')

    axs[1].plot(t, v)
    axs[1].set_title('v-t graf')
    axs[1].set(xlabel='vrijeme (s)', ylabel='brzina (m/s)')


    axs[2].plot(t, a)
    axs[2].set_title('a-t graf')
    axs[2].set(xlabel='vrijeme (s)', ylabel='akceleracija (m/s^2)')
    plt.show()



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

    fig, axs = plt.subplots(1, 3, figsize=(15, 4))

    axs[0].plot(x, y)
    axs[0].set_title("x-y graf")
    axs[0].set(xlabel='put (m)', ylabel='put (m)')

    axs[1].plot(t, x)
    axs[1].set_title('x-t graf')
    axs[1].set(xlabel='vrijeme (s)', ylabel='put (m)')

    axs[2].plot(t, y)
    axs[2].set_title('y-t graf')
    axs[2].set(xlabel='vrijeme (s)', ylabel='put (m)')
    plt.show()

   