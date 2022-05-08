import projectile as pr
import matplotlib.pyplot as plt


Cd_lista = []
m_lista = []

for i in range(100):
    Cd = i + 0.01
    Cd_lista.append(Cd)

for i in range(100):
    m = i + 0.01
    m_lista.append(m)

p1 = pr.Projectile(10, 40, 0, 0, 2, Cd, 1, m)#v0,theta,x0,y0,rho,Cd,A,m

domet1, domet2 = [], []

for el in Cd_lista:
    p1.Cd = el
    p1.set_initial_conditions(10, 40, 0, 0, 2, el, 1, 1)
    domet1.append(p1.runge_range(0.01))
    p1.reset()

p1.Cd = 0.1

for el in m_lista:
    p1.m = el
    p1.set_initial_conditions(10, 40, 0, 0, 2, 0.1, 1, el)
    domet2.append(p1.runge_range(0.01))
    p1.reset()


fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].plot(Cd_lista, domet1, color='#008080')
axes[0].set_title("Ovisnost dometa o koeficijentu trenja Cd")
axes[0].set_xlabel("Cd")
axes[0].set_ylabel("domet [m]")

axes[1].plot(m_lista, domet2, color='#008000')
axes[1].set_title("Ovisnost dometa o masi projektila")
axes[1].set_xlabel("m")
axes[1].set_ylabel("domet [m]")

plt.show()
