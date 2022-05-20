import projectile as pr
import matplotlib.pyplot as plt



p1 = pr.Projectile(10, 40, 0, 0, 2, 0.01, 1, 2)
            # v0, theta, x0, y0, rho, Cd, A, m
p1.set_initial_conditions(10, 40, 0, 0, 2, 0.01, 1, 2)
p1.range(0.1)
x_lista, y_lista = p1.euler(0.1)
p1.angle_to_hit_target(10, 10, 10, 0.1, 10, 2)



p2 = pr.Projectile(30, 40, 0, 0, 2, 0.01, 1, 2)
            # v0, theta, x0, y0, rho, Cd, A, m
p2.set_initial_conditions(30, 40, 0, 0, 2, 0.01, 1, 2)
p2.range(0.1)
x2, y2 = p2.euler(0.1)
p2.angle_to_hit_target(3, 10, 10, 0.1, 30, 2)



p3 = pr.Projectile(10, 40, 0, 0, 2, 0.01, 1, 2)
            # v0, theta, x0, y0, rho, Cd, A, m
p3.set_initial_conditions(10, 40, 0, 0, 2, 0.01, 1, 2)
p3.range(0.1)
x3, y3 = p3.euler(0.1)
p3.angle_to_hit_target(3, 8, 8, 0.1, 10, 2)
