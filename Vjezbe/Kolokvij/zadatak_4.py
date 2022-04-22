import projectiledrop as pd
import matplotlib.pyplot as plt
import numpy as np


p1 = pd.ProjectileDrop(2000, 200)
t1_lista, vy1_lista, vx1_lista, y1_lista, x1_lista = p1.euler(0.1)


p2 = pd.ProjectileDrop(2000, 200)
t2_lista, vy2_lista, vx2_lista, y2_lista, x2_lista = p1.euler(0.01)


# dt1 = [0.1]
# dt2 = [0.01]

# for i in dt1:
#     for el in range(100):
#         dt1.append(dt1[-1] + 0.1)

# for i in dt1:
#     for el in range(100):
#         dt2.append(dt2[-1] + 0.01)

dt = np.linspace(0, 100, 203)

plt.plot(t1_lista, dt)
plt.scatter(t2_lista, dt, color="m")
plt.title("t-dt graf")
plt.ylabel('vrijeme trajanja')
plt.xlabel('vremenski korak')

plt.show()