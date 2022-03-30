import particle as prt
import math as m
import matplotlib.pyplot as plt

# grafovi ovisnosti dometa i vremena trajanja gibanja o početnom kutu otklona 
# za neku odabranu i fiksiranu vrijednost početne brzine v0

p1 = prt.Particle(50, 0, 70, 30)


x_os = []
y_os = []
t_os = []

for kut in range(180):
    p1.set_initial_conditions(50, kut, 0, 0)
    x_os.append(kut)
    kut = (kut/180)*m.pi
    p1.theta = kut
    d = p1.range(0.01)
    t_br = p1.total_time(0.01)
    y_os.append(d)
    t_os.append(t_br)


fig, axes = plt.subplots(1, 2, figsize=(11, 4))

axes[0].plot(x_os, y_os, color='#9A0EEA')
axes[0].set(xlabel='angle [°]', ylabel='range [m]')

axes[1].plot(x_os, t_os)
axes[1].set(xlabel='angle [°]', ylabel='total time [s]')

plt.show()