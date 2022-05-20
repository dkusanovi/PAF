import matplotlib.pyplot as plt
import numpy as np
import math

class Particle:
    
    def __init__(self, E, B, v, q, m):
        self.E = E
        self.B = B
        self.v = v
        self.a = np.array([0, 0, 0])
        self.x = [0]
        self.y = [0]
        self.z = [0]
        self.t = [0]
        self.q = q
        self.m = m


    def reset(self):
        self.__init__(self.E, self.B, self.v, self.q, self.m)


    def __move(self, dt):
        self.t.append(self.t[-1] + dt)

        self.a = (self.q/self.m)*(self.E + np.cross(self.v, self.B))

        self.v = self.v + self.a*dt

        self.x.append(self.x[-1] + self.v[0]*dt)
        self.y.append(self.y[-1] + self.v[1]*dt)
        self.z.append(self.z[-1] + self.v[2]*dt)

    
    def range(self, dt, tuk):
        while self.t[-1] <= tuk:
            self.__move(dt)
        return self.x, self.y, self.z

    def runge_kutta(self, dt):
        self.t.append(self.t[-1] + dt)

        self.k1v = ((self.q/self.m)*(self.E + np.cross(self.v, self.B)))*dt
        self.k1 = self.v*dt

        self.k2v = ((self.q/self.m)*(self.E + np.cross(self.v + self.k1v/2, self.B)))*dt
        self.k2 = (self.v + self.k1v/2)*dt

        self.k3v = ((self.q/self.m)*(self.E + np.cross(self.v + self.k2v/2, self.B)))*dt
        self.k3 = (self.v + self.k2v/2)*dt

        self.k4v = ((self.q/self.m)*(self.E + np.cross(self.v + self.k3v, self.B)))*dt
        self.k4 = (self.v + self.k3v)*dt


        self.v = self.v + (1/6)*(self.k1v + 2*self.k2v + 2*self.k3v + self.k4v)

        self.x.append(self.x[-1] + (1/6)*(self.k1[0] + 2*self.k2[0] + 2*self.k3[0] + self.k4[0]))
        self.y.append(self.y[-1] + (1/6)*(self.k1[1] + 2*self.k2[1] + 2*self.k3[1] + self.k4[1]))
        self.z.append(self.z[-1] + (1/6)*(self.k1[2] + 2*self.k2[2] + 2*self.k3[2] + self.k4[2]))


    def runge_range(self, dt, tuk):
        while self.t[-1] <= tuk:
            self.runge_kutta(dt)
        return self.x, self.y, self.z
