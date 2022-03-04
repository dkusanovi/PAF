import matplotlib.pyplot as plt
import numpy as np

x1 = float(input("x os: "))
y1 = float(input("y os: "))
x2 = float(input("x os: "))
y2 = float(input("y os: "))

k = (y2-y1)/(x2-x1)
l = -k*x1 -y1

# Data for plotting
x = np.arange(-10, 10 , 0.01)
y = k*x + l

fig, ax = plt.subplots()
ax.plot(x, y)

ax.set(xlabel='x', ylabel='y',
       title='Jednadžba pravca')
ax.grid()

fig.savefig("test.png")
plt.show()