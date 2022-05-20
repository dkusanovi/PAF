import math
import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self, v0, theta, x0, y0, rho, Cd, A, m):
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
        self.rho = rho
        self.Cd = Cd
        self.A = A
        self.m = m


    def set_initial_conditions(self, v0, theta, x0, y0, rho, Cd, A, m):
        theta = (theta/180)*math.pi
        self.theta = theta
        self.v0 = v0
        self.x0 = x0
        self.y0 = y0

        self.rho = rho
        self.Cd = Cd
        self.A = A
        self.m = m

        self.t.append(0)
        self.x.append(0)
        self.y.append(0)
        self.vx.append(v0*(math.cos(self.theta)))
        self.vy.append(v0*(math.sin(self.theta)))
        self.ax.append(0)
        self.ay.append(9.81)


    def reset(self):
        self.__init__(self.v0, self.theta, self.x0, self.y0, self.rho, self.Cd, self.A, self.m)


    def __move(self, dt):

        self.t.append(self.t[-1] + dt)

        self.ax.append(-((self.rho*self.Cd*self.A)/(2*self.m))*(self.vx[-1])**2)
        self.ay.append(- self.g - ((self.rho*self.Cd*self.A)/(2*self.m))*(self.vy[-1])**2)
        
        self.vy.append(self.vy[-1] + self.ay[-1]*dt)
        self.vx.append(self.vx[-1] + self.ax[-1]*dt)
        
        self.x.append(self.x[-1] + self.vx[-1]*dt)
        self.y.append(self.y[-1] + self.vy[-1]*dt)
        

    def range(self, dt):
        while self.y[-1] >= 0:
            self.__move(dt)
        return self.x[-1]


    def euler(self, dt):
        self.range(dt)
        return self.x, self.y


    def plot_trajectory(self):
        plt.plot(self.x, self.y)
        plt.title("x-y graf")
        plt.xlabel('put (m)')
        plt.ylabel('put (m)')
        plt.show()


    def analitical(self):
        return ((self.v0**2)*math.sin(2*self.theta))/9.81


    def printInfo(self):
        while self.y[-1] >= 0:
            self.__move()
        print("Za v =", self.v0, "i kut", self.theta, "domet je", self.x[-1], "m.")


    def akceleracija(self, x, v, t):
        return -((self.rho*self.Cd*self.A)/(2*self.m))*(self.vx[-1])*abs((self.vx[-1]))

    def akc(self, y, v, t):
        return - self.g - ((self.rho*self.Cd*self.A)/(2*self.m))*(self.vy[-1])*abs(self.vy[-1])


    def runge_kutta(self, dt):

        # x
        self.k1vx = self.akceleracija(self.x[-1], self.vx[-1], self.t[-1])*dt
        self.k1x = self.vx[-1]*dt

        self.k2vx = self.akceleracija((self.x[-1] + self.k1x/2), (self.vx[-1] + self.k1vx/2), (self.t[-1] + dt/2))*dt
        self.k2x = (self.vx[-1] + self.k1vx/2)*dt

        self.k3vx = self.akceleracija((self.x[-1] + self.k2x/2), (self.vx[-1] + self.k2vx/2), (self.t[-1] + dt/2))*dt
        self.k3x = (self.vx[-1] + self.k2vx/2)*dt

        self.k4vx = self.akceleracija((self.x[-1] + self.k3x), (self.vx[-1] + self.k3vx), (self.t[-1] + dt))* dt
        self.k4x = (self.vx[-1] + self.k3vx)*dt

        self.vx.append(self.vx[-1] + (1/6)*(self.k1vx + 2*self.k2vx + 2*self.k3vx + self.k4vx))
        self.x.append(self.x[-1] + (1/6)*(self.k1x + 2*self.k2x + 2*self.k3x + self.k4x))

        # y
        self.k1vy = self.akc(self.y[-1], self.vy[-1], self.t[-1])*dt
        self.k1y = self.vy[-1]*dt

        self.k2vy = self.akc((self.y[-1] + self.k1y/2), (self.vy[-1] + self.k1vy/2), (self.t[-1] + dt/2))*dt
        self.k2y = (self.vy[-1] + self.k1vy/2)*dt

        self.k3vy = self.akc((self.y[-1] + self.k2y/2), (self.vy[-1] + self.k2vy/2), (self.t[-1] + dt/2))*dt
        self.k3y = (self.vy[-1] + self.k2vy/2)*dt

        self.k4vy = self.akc((self.y[-1] + self.k3y), (self.vy[-1] + self.k3vx), (self.t[-1] + dt))* dt
        self.k4y = (self.vy[-1] + self.k3vx)*dt

        self.vy.append(self.vy[-1] + (1/6)*(self.k1vy + 2*self.k2vy + 2*self.k3vy + self.k4vy))
        self.y.append(self.y[-1] + (1/6)*(self.k1y + 2*self.k2y + 2*self.k3y + self.k4y))


    def runge_range(self, dt):
        while self.y[-1] >= 0:
            self.runge_kutta(dt)
        return self.x[-1]


    def runge(self, dt):
        self.runge_range(dt)
        return self.x, self.y


    def kugla_kocka(self, ili, r, a):
        if ili == "kugla":
            self.A = r**2*math.pi

        elif ili == "kocka":
            self.theta = (math.atan(self.vy[-1]/self.vx[-1]))
            self.A = a**2*(math.cos(self.theta) + math.sin(self.theta))



    def angle_to_hit_target(self, radijus, x_m, y_m, dt):
        self.radijus = radijus
        self.x_m = x_m
        self.y_m = y_m
        self.v0 = 0
        angle_to_hit_target = 0
        kut = 0
        j = True

        while j:
            udaljenost = []
            self.reset()
            self.set_initial_conditions(30, kut, 0, 0, 2, 0.01, 1, 1)

            while self.y[-1] >= 0:
                self.runge_kutta(dt)


            for i in range(len(self.y)):
                udaljenost.append(math.sqrt((y_m-self.y[i])**2+(x_m-self.x[i])**2)-radijus)

            for el in udaljenost:
                if el <= 0:
                    angle_to_hit_target = kut
                    j = False
                    break
            
            kut = kut + 0.1
            if kut > 90:
                break

        krug = plt.Circle((self.x_m, self.y_m), self.radijus, fill=False)
        fig, ax = plt.subplots()
        ax.add_patch(krug)
        ax.plot(self.x, self.y)
        
        plt.show()

        if angle_to_hit_target > 0:
            print("Početni kut da se pogodi meta je", angle_to_hit_target, "°.")
        else:
            print("Objekt nikada neće pogoditi metu.")