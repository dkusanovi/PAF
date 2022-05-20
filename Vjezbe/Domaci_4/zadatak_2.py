import projectile as pr
import matplotlib.pyplot as plt

p1 = pr.Projectile(10, 40, 0, 0, 2, 0.01, 1, 2)
            # v0, theta, x0, y0, rho, Cd, A, m

p1.set_initial_conditions(10, 40, 0, 0, 2, 0.01, 1, 2)

p1.range(0.1)

x_lista, y_lista = p1.euler(0.1)

p1.angle_to_hit_target(3, 10, 10, 0.1)
