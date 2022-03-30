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
        self.vx.append(self.vx[-1]+self.ax[-1]*dt)
        self.x.append(self.x[-1] + self.vx[-1]*dt)
        self.y.append(self.y[-1] + self.vy[-1]*dt)
        

    def range(self, dt):
        while self.y[-1] >= 0:
            self.__move(dt)
        return self.x[-1]


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
            self.__move()
        print("Za v =", self.v0, "i kut", self.theta, "domet je", self.x[-1], "m.")

    
    def total_time(self, dt):
        return len(self.vy)*dt


    def max_speed(self):
        self.vy.sort()
        v_max = m.sqrt(self.vy[-1]**2+self.vx[-1]**2)
        print(v_max)


    def velocity_to_hit_target(self, r, x_m, y_m, dt): 
        #radijus, koordinate tocke, dt
        self.r = r
        self.x_m = x_m
        self.y_m = y_m
        self.v0 = 0
        velocity_to_hit_target = []

        while True:
            udaljenost = []

            while self.y[-1] >= 0:
                self.__move(dt)      

            for i in range(len(self.y)):
                udaljenost.append(m.sqrt((y_m-self.y[i])**2+(x_m-self.x[i])**2)-r)

            for el in udaljenost:
                if el <= r:
                    velocity_to_hit_target.append(self.v0)
                    break 
                else:
                    break
            
            self.v0 = self.v0 + 0.1
            if self.v0 > 50:
                break

            # print(velocity_to_hit_target)
            # print(self.y_m)


    def angle_to_hit_target(self, r, x_m, y_m, dt):
        self.r = r
        self.x_m = x_m
        self.y_m = y_m
        self.theta = 0
        angle_to_hit_target = []

        while True:
            udaljenost = []

            while self.y[-1] >= 0:
                self.__move(dt)      

            for i in range(len(self.y)):
                udaljenost.append(m.sqrt((self.y[i]-y_m)**2+(self.x[i]-x_m)**2)-r)

            for el in udaljenost:
                if el <= r:
                    angle_to_hit_target.append(self.theta)
                    break 
                else: 
                    break 
            
            self.theta = self.theta + 0.1
            if self.theta > 90:
                break

            # print(angle_to_hit_target)
            # print(self.y_m)


# p1 = Particle(0, 40, 0, 0)

# p1.set_initial_conditions(0, 40, 0, 0)
# p1.velocity_to_hit_target(3, 5, 2, 0.1)

# velocity_to_hit_target() za zadani kut računa potrebnu početnu brzinu da se pogodi kuglica
# angle_to_hit_target() za zadanu početnu brzinu računa kut da se pogodi kuglica