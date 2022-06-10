import universe
import matplotlib.pyplot as plt
import numpy as np
import math

au = 1.496e11
day = 60*60*24
year = 365.242*day

#name, mass, xy, v, color
sun = universe.Planet("Sun", 1.989e30, np.array([0, 0]), np.array([0, 0]), "magenta")
mercury = universe.Planet("Mercury", 3.3e24, np.array([0, 0.466*au]), np.array([-47362, 0]), "orange")
venus = universe.Planet("Venus", 4.8685e24, np.array([0.723*au, 0]), np.array([0, -35020]), "brown")
earth = universe.Planet("Earth", 5.9742e24, np.array([-au, 0]), np.array([0, -29783]), "blue")
mars = universe.Planet("Mars", 6.417e23, np.array([0, -1.666*au]), np.array([24007, 0]), "red")
# jupiter = universe.Planet("Jupiter", 1.898e27, np.array([0, -5.2*au]), np.array([13070, 0]), "green")
# saturn = universe.Planet("Saturn", 5.683e26, np.array([0, 9.5*au]), np.array([9690, 0]), "pink")
# uranus = universe.Planet("Uranus", 8.681e25 , np.array([19.8*au, 0]), np.array([0, 6810]), "black")
# neptune = universe.Planet("Neptune", 1.024e26, np.array([0, 30*au]), np.array([5430, 0]), "#0123")

solar_system = universe.Universe()
solar_system.add_planets(sun)
solar_system.add_planets(earth)
solar_system.add_planets(mercury)
solar_system.add_planets(venus)
solar_system.add_planets(mars)
# solar_system.add_planets(jupiter)
# solar_system.add_planets(saturn)
# solar_system.add_planets(uranus)
# solar_system.add_planets(neptune)



x, y = solar_system.evolve(5*year, 3600)

plt.figure(figsize=(5.5, 5.5))

for i in range(len(solar_system.planets)):

    plt.plot(x[i], y[i], color=solar_system.planets[i].color)
    plt.legend(["Sunce", "Merkur", "Venera", "Zemlja", "Mars"])
    # plt.legend(["Sunce", "Merkur", "Venera", "Zemlja", "Mars", "Jupiter", "Saturn", "Uran", "Neptun"])
    plt.title("x-y graf")
    plt.xlabel("x")
    plt.ylabel("y")

plt.show()