import math
from re import X
import matplotlib.pyplot as plt


class ProjectileDrop():

    def __init__(self, y0, vx0):
        self.vx0 = vx0
        self.vx = [vx0]
        self.vy = [0]
        self.y0 = y0
        self.y = [self.y0]
        self.x = [0]
        self.ax = [0]
        self.t = [0]
        
        print("Objekt je uspjesno stvoren. Pocetna brzina objekta je", self.vx0, "m/s, a visina", self.y0, "m.")


    def reset(self):
        self.__init__(self.y0, self.vx0)


    def change_height(self, y0):
        self.reset()
        self.y0 = y0
        print("Nova visina projektila je", self.y0, ".")


    def change_velocity(self, vx0):
        self.reset()
        self.vx0 = vx0
        print("Nova brzina projektila je", self.vx0, ".")



    def __move(self, dt):
        g = 9.81
        self.t.append(self.t[-1] + dt)
        self.vy.append(self.vy[-1] - g*dt)
        self.vx.append(self.vx[-1] + self.ax[-1]*dt)
        self.y.append(self.y[-1] + self.vy[-1]*dt)
        self.x.append(self.x[-1] + self.vx[-1]*dt)


    def euler(self, dt):
        
        while self.y[-1] >= 0:
            self.__move(dt)

        return self.t, self.vy, self.vx, self.y, self.x



    def time(self, dt):
        self.reset()

        while self.y[-1] >= 0:
            self.__move(dt) 

        return print("Vrijeme padanja sa dt =", dt, "iznosi", self.t[-1], "s.")


    def __vjetar(self, dt, vxv):
        g = 9.81
        self.t.append(self.t[-1] + dt)
        self.vx.append((self.vx[-1]+vxv) + self.ax[-1]*dt)
        self.vy.append(self.vy[-1] - g*dt)
        self.y.append(self.y[-1] + self.vy[-1]*dt)
        self.x.append(self.x[-1] + (self.vx[-1])*dt)



    def euler2(self, dt):
        self.reset()
        while self.y[-1] >= 0:
            self.__vjetar(dt, 20) # brzina vjetra 20

        return self.t, self.vy, self.vx, self.y, self.x



    def to_hit_target(self, r, x_m, y_m, vxv, dt): 
            #radijus, koordinate mete, brzina vjetra, dt
            self.x_m = x_m
            self.y_m = y_m
            self.r = r
            udaljenost = []
            self.euler2(0.1)

            for i in range(len(self.y)):
                udaljenost.append(math.sqrt((y_m-self.y[i])**2+(x_m-self.x[i])**2)-r)

            for el in udaljenost:
                if el <= 0:
                    break

            while self.y0 <= 0:
                self.__vjetar(dt, vxv)
                break

            krug = plt.Circle((self.x_m, self.y_m), self.r, fill=False)
            fig, ax = plt.subplots()
            ax.add_patch(krug)
            ax.plot(self.x, self.y)
            
            plt.show()


