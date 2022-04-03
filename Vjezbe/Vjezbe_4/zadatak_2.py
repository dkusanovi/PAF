import calculus as cal
import matplotlib.pyplot as plt

x_os = []

for i in range(1, 20, 1):
    x_os.append(50*i)

y_os = []
y_os2 = []
y_os3 = []
y_os4 = []

for i in x_os:
    donja, gornja = cal.integrate(cal.fun, 0, 1, i)
    integral = cal.i_fun(1) - cal.i_fun(0)
    trap = cal.trapez(cal.fun, 0, 1, i)

    y_os.append(donja)
    y_os2.append(gornja)
    y_os3.append(integral)
    y_os4.append(trap)

plt.scatter(x_os, y_os, color = "red")
plt.scatter(x_os, y_os2, color = "blue")
plt.plot(x_os, y_os3, color = "green")
plt.scatter(x_os, y_os4, color = "black")

plt.show()