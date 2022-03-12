import numpy as np
import matplotlib.pyplot as plt
import math as m

v0 = 15
theta = m.pi/3
t = 10
g = 9.81
dt = 0.01

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

fig, axs = plt.subplots(1, 3, figsize=(13, 4))

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