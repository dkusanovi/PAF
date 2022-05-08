import projectile as pr


p1 = pr.Projectile(10, 40, 0, 0, 2, 0.01, 1, 2)
            # v0, theta, x0, y0, rho, Cd, A, m

p1.set_initial_conditions(10, 40, 0, 0, 2, 0.01, 1, 2)

p1.range(0.01)

p1.plot_trajectory()

