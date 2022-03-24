import math as m
import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, v0, theta, x0, y0):
        self.x = []
        self.y = []
        self.t = []
        self.dt = 0.01
        self.vx = []
        self.vy = []
        self.ax = []
        self.ay = []
        self.g = 9.81
        # self.v0 = v0
        # self.theta = theta
        # self.x0 = x0
        # self.y0 = y0


    def set_initial_conditions(self, v0, theta, x0, y0):
        theta = (theta/180)*m.pi
        self.theta = theta
        self.v0 = v0

        self.t.append(0)
        self.x.append(0)
        self.y.append(0)
        self.vx.append(v0*(m.cos(self.theta)))
        self.vy.append(v0*(m.sin(self.theta)))
        self.ax.append(0)
        self.ay.append(9.81)
        #self.dt.append(0.01)


    def reset(self):
        self.__init__()

    def __move(self): # privatna sa __
        self.t.append(self.t[-1]+self.dt)
        self.vy.append(self.vy[-1] - self.g*self.dt)
        self.vx.append(self.vx[-1]+self.ax[-1]*self.dt)
        self.x.append(self.x[-1] + self.vx[-1]*self.dt)
        self.y.append(self.y[-1] + self.vy[-1]*self.dt)
        

    def range(self, dt):
        while self.y[-1] >= 0:
            self.__move()
        return self.x[-1]


    def plot_trajectory(self):
        # for i in range(1000):
            # self.x.append(self.x[i] + self.vx[i]*self.dt)
            # self.y.append(self.y[i] + self.vy[i]*self.dt)

        plt.plot(self.x, self.y)
        plt.title("x-y graf")
        plt.xlabel('put (m)')
        plt.ylabel('put (m)')
        plt.show()


    def analitical(self):
        self.x.append(((self.v0**2)*m.sin(2*self.theta))/9.81)
        return self.x[-1]


    def printInfo(self):
        while self.y[-1] >= 0:
            self.__move()
        print("Za v =", self.v0, "i kut", self.theta, "domet je", self.x[-1], "m.")


p1 = Particle(10, 40, 0, 0)
p1.set_initial_conditions(10, 40, 0, 0)
p1.analitical()