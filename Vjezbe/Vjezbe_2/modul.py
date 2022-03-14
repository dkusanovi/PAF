import matplotlib.pyplot as plt
import numpy as np
import math as m


def kosi_hitac(v0, theta, t_uk, g, dt):

    theta = (theta/180)*m.pi
    preciznost = round(t_uk / dt)
    brojac = 0

    x_br = 0
    y_br = 0
    t_br = 0
    x = [x_br]
    y = [y_br]
    t = [t_br]

    v0x = v0*(m.cos(theta))
    v0y = v0*(m.sin(theta))
    vy = v0y

    for i in range(preciznost):
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
        brojac = brojac + 1
    
    plt.plot(x, y)
    plt.ylim(0)
    plt.xlim(0, x[brojac])
    plt.title("x-y graf")
    plt.xlabel('put (m)')
    plt.ylabel('put (m)')
    plt.show()


# kosi_hitac(50, 40, 10, 9.81, 0.01)


def maks_visina(v0, theta, g, dt):
    theta = (theta/180)*m.pi
    v0y = v0*(m.sin(theta))
    vy = v0y
    h = 0

    while vy > 0:
        vy = vy - g*dt
        h = h + vy*dt

    print(h)

# maks_visina(50, 35, 9.81, 0.01)


def domet(v0, theta, t_uk, g, dt):
    theta = (theta/180)*m.pi
    preciznost = round(t_uk / dt)
    brojac = 0

    x_br = 0
    y_br = 0
    t_br = 0
    x = [x_br]
    y = [y_br]
    t = [t_br]

    v0x = v0*(m.cos(theta))
    v0y = v0*(m.sin(theta))
    vy = v0y

    for i in range(preciznost):
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
        brojac = brojac + 1 

    print("Domet je", x[brojac])


# domet(40, 87, 17, 9.81, 0.01)

def maks_brzina(v0, theta, t_uk, g, dt):
    theta = (theta/180)*m.pi
    preciznost = round(t_uk / dt)
    brojac = 0

    x_br = 0
    y_br = 0
    t_br = 0
    x = [x_br]
    y = [y_br]
    t = [t_br]

    v0x = v0*(m.cos(theta))
    v0y = v0*(m.sin(theta))
    vy_br = v0y
    vy = [v0y]
    

    for i in range(preciznost):
        t_br = t_br + dt
        x_br = x_br + v0x*dt
        vy_br = vy_br - g*dt
        y_br = y_br + vy_br*dt
        x.append(x_br)
        y.append(y_br)
        t.append(t_br)
        vy.append(vy_br)

    vy.sort()
    v_max = m.sqrt(vy[-1]*2+v0x*2)
    #print("Maksimalna je brzina", vy[-1])
    print("Maksimalna je brzina", v_max)

# maks_brzina(15, 60, 10, 9.81, 0.01)