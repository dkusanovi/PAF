import matplotlib.pyplot as plt


x_lista = []
v_lista = []
a_lista = []
t_lista = []

with open("x.txt", 'r') as fh:
    for el in fh:
        x_lista.append(float(el))

with open("v.txt", 'r') as fh:
    for el in fh:
        v_lista.append(float(el))

with open("a.txt", 'r') as fh:
    for el in fh:
        a_lista.append(float(el))

with open("t.txt", 'r') as fh:
    for el in fh:
        t_lista.append(float(el))


fig, axes = plt.subplots(1, 3, figsize=(13, 4))

axes[0].plot(t_lista, x_lista)
axes[0].set(xlabel='t [s]', ylabel='x [m]')
axes[1].plot(t_lista, v_lista)
axes[1].set(xlabel='t [s]', ylabel='v [m/s]')
axes[2].plot(t_lista, a_lista)
axes[2].set(xlabel='t [s]', ylabel='a [m/s**2]')

plt.show()