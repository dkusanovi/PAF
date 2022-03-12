import matplotlib.pyplot as plt
import numpy as np
import math as m


F = 50
m = 2
t = 10
deltat = 0.01

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