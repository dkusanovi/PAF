import projectile as pr
import matplotlib.pyplot as plt


# kugla

p1 = pr.Projectile(10, 40, 0, 0, 2, 0.01, 1, 2)
            # v0, theta, x0, y0, rho, Cd, A, m

p1.set_initial_conditions(10, 40, 0, 0, 2, 0.01, 1, 2)
p1.kugla_kocka("kugla", 0.3, 0.3)

p2 = pr.Projectile(10, 40, 0, 0, 2, 0.01, 1, 2)
            # v0, theta, x0, y0, rho, Cd, A, m

p2.set_initial_conditions(10, 40, 0, 0, 2, 0.01, 1, 2)
p2.kugla_kocka("kugla", 0.3, 0.3)

x1, y1 = p1.euler(0.01)
x2, y2 = p2.runge(0.01)



# kocka

p3 = pr.Projectile(10, 40, 0, 0, 2, 0.01, 1, 2)
            # v0, theta, x0, y0, rho, Cd, A, m

p3.set_initial_conditions(10, 40, 0, 0, 2, 0.01, 1, 2)
p3.kugla_kocka("kocka", 0.3, 0.3)

p4 = pr.Projectile(10, 40, 0, 0, 2, 0.01, 1, 2)
            # v0, theta, x0, y0, rho, Cd, A, m

p4.set_initial_conditions(10, 40, 0, 0, 2, 0.01, 1, 2)
p4.kugla_kocka("kocka", 0.3, 0.3)

x3, y3 = p3.euler(0.01)
x4, y4 = p4.runge(0.01)



fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].plot(x1, y1)
axes[0].plot(x2, y2, color="m")
axes[0].set_title("Kugla")

axes[1].plot(x3, y3)
axes[1].plot(x4, y4, color="m")
axes[1].set_title("Kocka")

plt.show()