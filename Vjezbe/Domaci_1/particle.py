import math as m
import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, v0, theta, x0, y0):
        self.x = []
        self.y = []
        self.t = []
        self.vx = []
        self.vy = []
        self.ax = []
        self.ay = []
        self.g = 9.81
        self.v0 = v0
        self.theta = theta
        self.x0 = x0
        self.y0 = y0


    def set_initial_conditions(self, v0, theta, x0, y0):
        theta = (theta/180)*m.pi
        self.theta = theta
        self.v0 = v0
        self.x0 = x0
        self.y0 = y0

        self.x = []
        self.y = []
        self.t = []
        self.vx = []
        self.vy = []
        self.ax = []
        self.ay = []

        self.t.append(0)
        self.x.append(0)
        self.y.append(0)
        self.vx.append(v0*(m.cos(self.theta)))
        self.vy.append(v0*(m.sin(self.theta)))
        self.ax.append(0)
        self.ay.append(9.81)


    def reset(self):
        self.__init__(self.v0, self.theta, self.x0, self.y0)

    def __move(self, dt): # privatna sa __
        self.t.append(self.t[-1]+dt)
        self.vy.append(self.vy[-1] - self.g*dt)
        self.vx.append(self.vx[-1] + self.ax[-1]*dt)
        self.x.append(self.x[-1] + self.vx[-1]*dt)
        self.y.append(self.y[-1] + self.vy[-1]*dt)
        

    def range(self, dt):
        while self.y[-1] >= 0:
            self.__move(dt)
        #if self.x[i] < 0
        return abs(self.x[-1])


    def plot_trajectory(self):
        plt.plot(self.x, self.y)
        plt.title("x-y graf")
        plt.xlabel('put (m)')
        plt.ylabel('put (m)')
        plt.show()


    def analitical(self):
        return ((self.v0**2)*m.sin(2*self.theta))/9.81


    def printInfo(self):
        while self.y[-1] >= 0:
            self.__move(0.1)
        print("Za v =", self.v0, "i kut", self.theta, "domet je", self.x[-1], "m.")

    
    def total_time(self):
        return self.t[-1]


    def max_speed(self):
        self.vy.sort()
        v_max = m.sqrt(self.vy[-1]**2+self.vx[-1]**2)
        return v_max


    def velocity_to_hit_target(self, r, x_m, y_m, dt): 
        #radijus, koordinate tocke, dt
        self.r = r
        self.x_m = x_m
        self.y_m = y_m
        self.v0 = 0
        velocity_to_hit_target = 0
        brzina = 0
        j = True

        while j:
            udaljenost = []
            self.set_initial_conditions(brzina, 30, 0, 0)

            while self.y[-1] >= 0:
                self.__move(dt)


            for i in range(len(self.y)):
                udaljenost.append(m.sqrt((y_m-self.y[i])**2+(x_m-self.x[i])**2)-r)

            for el in udaljenost:
                if el <= 0:
                    velocity_to_hit_target = brzina
                    j = False
                    break
            
            brzina = brzina + 0.1
            if brzina > 100:
                break

        krug = plt.Circle((self.x_m, self.y_m), self.r, fill=False)
        fig, ax = plt.subplots()
        ax.add_patch(krug)
        ax.plot(self.x, self.y)
        
        plt.show()


        print("Početna brzina da se pogodi kuglica je", velocity_to_hit_target, "m/s.")


    def angle_to_hit_target(self, r, x_m, y_m, dt):
        self.r = r
        self.x_m = x_m
        self.y_m = y_m
        self.v0 = 0
        angle_to_hit_target = 0
        kut = 0
        j = True

        while j:
            udaljenost = []
            self.set_initial_conditions(10, kut, 0, 0)

            while self.y[-1] >= 0:
                self.__move(dt)


            for i in range(len(self.y)):
                udaljenost.append(m.sqrt((y_m-self.y[i])**2+(x_m-self.x[i])**2)-r)

            for el in udaljenost:
                if el <= 0:
                    angle_to_hit_target = kut
                    j = False
                    break
            
            kut = kut + 0.1
            if kut > 90:
                break

        krug = plt.Circle((self.x_m, self.y_m), self.r, fill=False)
        fig, ax = plt.subplots()
        ax.add_patch(krug)
        ax.plot(self.x, self.y)
        
        plt.show()


        print("Početni kut da se pogodi kuglica je", angle_to_hit_target, "°.")
