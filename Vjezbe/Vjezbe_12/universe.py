import matplotlib.pyplot as plt
import numpy as np
import math

class Planet:
    def __init__(self, name, mass, xy, v, color):
        self.name = name
        self.mass = mass
        self.xy = xy
        self.v = v
        self.color = color
        self.x = [xy[0]]
        self.y = [xy[1]]
        self.a = np.array([0, 0])

    

class Universe:
    def __init__(self):
        self.planets = []
        self.G = 6.67408*10**(-11)
        self.t = 0


    def add_planets(self, p):
        self.planets.append(p)


    def __move(self, dt):
        self.t = self.t + dt

        for planet1 in self.planets:
            planet1.a = np.array([0, 0])
            for planet2 in self.planets:
                if planet1 != planet2:
                    d = (planet1.xy - planet2.xy)**2
                    n = math.sqrt(d[0] + d[1])
                    planet1.a = planet1.a - self.G*(planet2.mass / n**3 )*(planet1.xy - planet2.xy)

            planet1.v = planet1.v + planet1.a*dt
            planet1.xy = planet1.xy + planet1.v*dt

            planet1.x.append(planet1.xy[0])
            planet1.y.append(planet1.xy[1])
        
    
    def evolve(self, tuk, dt):
        step = round(tuk/dt)
        br = 0
        while br < step:
            self.__move(dt)
            br = br + 1
        x, y = [], []
        for planet1 in self.planets:
            x.append(planet1.x)
            y.append(planet1.y)

        return x, y
