import planet as p
import matplotlib.pyplot as plt
import numpy as np

sunce_zemlja = p.Planet(np.array([1.486*10**(11), 0]), np.array([0.1, 0.1]), np.array([0, 29783]), np.array([0, 0]), np.array([0, 0]), np.array([0, 0]), 5.9742*10**(24), 1.989*10**(30))
                # r1, r2, v1, v2, a1, a2, m1, m2
x1, y1, x2, y2 = sunce_zemlja.range(100)

plt.figure(figsize=(5.5, 5.5))
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.legend(["Zemlja", "Sunce"])
plt.title("x-y graf")
plt.xlabel("x")
plt.ylabel("y")
plt.show()