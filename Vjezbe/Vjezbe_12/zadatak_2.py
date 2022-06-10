import matplotlib.animation as animation
import universe
import matplotlib.pyplot as plt
import numpy as np
import math

au = 1.496e11
day = 60*60*24
year = 365.242*day

xsun, ysun = [], []
xmercury, ymercury = [], []
xvenus, yvenus = [], []
xearth, yearth = [], []
xmars, ymars = [], []
xjupiter, yjupiter = [], []

#name, mass, xy, v, color
sun = universe.Planet("Sun", 1.989e30, np.array([0, 0]), np.array([0, 0]), "magenta")
mercury = universe.Planet("Mercury", 3.3e24, np.array([0, 0.466*au]), np.array([-47362, 0]), "orange")
venus = universe.Planet("Venus", 4.8685e24, np.array([0.723*au, 0]), np.array([0, -35020]), "brown")
earth = universe.Planet("Earth", 5.9742e24, np.array([-au, 0]), np.array([0, -29783]), "blue")
mars = universe.Planet("Mars", 6.417e23, np.array([0, -1.666*au]), np.array([24007, 0]), "red")
jupiter = universe.Planet("Jupiter", 1.898e27, np.array([0, -5.2*au]), np.array([13070, 0]), "green")

solar_system = universe.Universe()
solar_system.add_planets(sun)
solar_system.add_planets(earth)
solar_system.add_planets(mercury)
solar_system.add_planets(venus)
solar_system.add_planets(mars)
solar_system.add_planets(jupiter)

x, y = solar_system.evolve(5*year, 36000)


plt.style.use("dark_background")
fig = plt.figure(figsize=[6, 6])
ax = plt.axes([0., 0., 1., 1.], xlim=(-1.8, 1.8), ylim=(-1.8, 1.8))
ax = plt.axes(xlim=(-850000000000, 800000000000), ylim=(-800000000000, 800000000000))
line, = ax.plot([], [], lw = 2)
ax.set_aspect('equal')
ax.axis('off')


linesun, = ax.plot([], [],'o',color = sun.color)
line1, = ax.plot([], [],'o',color = mercury.color)
line2, = ax.plot([], [], 'o',color = venus.color)
line3, = ax.plot([], [], 'o',color = earth.color)
line4, = ax.plot([], [], 'o',color = mars.color)
line5, = ax.plot([], [], 'o',color = jupiter.color)



def init():
    linesun.set_data([],[])
    line1.set_data([],[])
    line2.set_data([],[])
    line3.set_data([],[])
    line4.set_data([],[])
    line5.set_data([],[])
    return line, line1, line2, line3, line4, line5

def animate(i):
    xsun.append(sun.x[i])
    ysun.append(sun.y[i])

    xmercury.append(mercury.x[i])
    ymercury.append(mercury.y[i])

    xvenus.append(venus.x[i])
    yvenus.append(venus.y[i])

    xearth.append(earth.x[i])
    yearth.append(earth.y[i])

    xmars.append(mars.x[i])
    ymars.append(mars.y[i])

    xjupiter.append(jupiter.x[i])
    yjupiter.append(jupiter.y[i])

    linesun.set_data(xsun[i], ysun[i])
    line1.set_data(xmercury[i], ymercury[i])
    line2.set_data(xvenus[i], yvenus[i])
    line3.set_data(xearth[i], yearth[i])
    line4.set_data(xmars[i], ymars[i])
    line5.set_data(xjupiter[i], yjupiter[i])

    return line, line1, line2, line3, line4, line5

plt.plot(sun.x, sun.y, label=sun.name, color=sun.color)
plt.plot(mercury.x, mercury.y, label=mercury.name, color=mercury.color)
plt.plot(venus.x, venus.y, label=venus.name,color=venus.color)
plt.plot(earth.x, earth.y, label=earth.name, color=earth.color)
plt.plot(mars.x,mars.y,label=mars.name,color=mars.color)
plt.plot(jupiter.x, jupiter.y, label=jupiter.name,color=jupiter.color)

anim = animation.FuncAnimation(fig, animate, init_func=init, interval=25)
plt.show()


# https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/