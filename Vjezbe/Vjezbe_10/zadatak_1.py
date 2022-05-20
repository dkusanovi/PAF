import particle as prt
import numpy as np
import matplotlib.pyplot as plt


p1 = prt.Particle(np.array([0., 0., 0.]), np.array([0., 0., 1.]), np.array([0.1, 0.1, 0.1]), 1, 1)
                # E, B, v, q, m
x1, y1, z1 = p1.range(0.01, 18)

p1 = prt.Particle(np.array([0., 0., 0.]), np.array([0., 0., 1.]), np.array([0.1, 0.1, 0.1]), -1, 1)
                # E, B, v, q, m
x2, y2, z2 = p1.range(0.01, 18)


fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(x1, y1, z1, c="r", label="positron")
ax.plot3D(x2, y2, z2, c="b", label="electron")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.view_init(30, 30)
plt.legend()
plt.show()