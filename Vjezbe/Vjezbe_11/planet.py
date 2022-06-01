import matplotlib.pyplot as plt
import numpy as np
import math

class Planet:
    
    def __init__(self, r1, r2, v1, v2, a1, a2, m1, m2):
        self.r1 = r1
        self.r2 = r2
        self.v1 = v1
        self.v2 = v2
        self.a1 = a1
        self.a2 = a2
        self.x1 = [1.486*10**(11)]
        self.y1 = [0]
        self.x2 = [0]
        self.y2 = [0]
        self.t = [0]
        self.m1 = m1  # mz
        self.m2 = m2  # ms
        self.G = 6.67408*10**(-11)
        self.tuk = 365.242*24*3600


    def reset(self):
        self.__init__(self.r1, self.r2, self.v1, self.v2, self.a1, self.a2, self.m1, self.m2)


    def __move(self, dt):
        d1 = (self.r1 - self.r2)**2
        d2 = (self.r2 - self.r1)**2
        n1 = math.sqrt(d1[0] + d1[1])
        n2 = math.sqrt(d2[0] + d2[1])

        self.t.append(self.t[-1] + dt)

        self.a1 = -self.G*(self.m2 / n1**3 )*(self.r1 - self.r2)
        self.a2 = -self.G*(self.m1 / n2**3 )*(self.r2 - self.r1)

        self.v1 = self.v1 + self.a1*dt
        self.v2 = self.v2 + self.a2*dt

        self.r1 = self.r1 + self.v1*dt
        self.r2 = self.r2 + self.v2*dt

        self.x1.append(self.r1[0])
        self.y1.append(self.r1[1])
        self.x2.append(self.r2[0])
        self.y2.append(self.r2[1])

    
    def range(self, dt):
        while self.t[-1] <= self.tuk:
            self.__move(dt)
        return self.x1, self.y1, self.x2, self.y2