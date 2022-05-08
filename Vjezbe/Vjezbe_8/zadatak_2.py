from turtle import color
import projectile as pr
import matplotlib.pyplot as plt



p1 = pr.Projectile(10, 40, 0, 0, 2, 0.01, 1, 2)
            # v0, theta, x0, y0, rho, Cd, A, m

p1.set_initial_conditions(10, 40, 0, 0, 2, 0.01, 1, 2)
#p1.range(0.01)
x_lista, y_lista = p1.euler(0.01)



p2 = pr.Projectile(10, 40, 0, 0, 2, 0.01, 1, 2)
            # v0, theta, x0, y0, rho, Cd, A, m

p2.set_initial_conditions(10, 40, 0, 0, 2, 0.01, 1, 2)
#p2.runge_range(0.01)
x2_lista, y2_lista = p2.runge(0.01)



fig, ax = plt.subplots()

ax.plot(x_lista, y_lista)
ax.plot(x2_lista, y2_lista, color="m")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(["Eulerova metoda", "Runge-Kutta 4. reda"])

plt.show()