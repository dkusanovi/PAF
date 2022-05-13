import math
import matplotlib.pyplot as plt
import numpy as np


class BungeeJumping:

    def __init__(self, h0, k, m, dt, rho, Cd, A, l0):
        self.y = []
        self.t = []
        self.vy = []
        self.ay = []

        self.Ep = []
        self.Ek = []
        self.Eel = []
        self.Euk = []

        self.g = 9.81
        self.h0 = h0
        self.k = k
        self.m = m
        self.dt = dt
        self.rho = rho
        self.Cd = Cd
        self.A = A
        self.l0 = l0


    def set_initial_conditions(self, h0, k, m, dt, rho, Cd, A, l0):
        self.h0 = h0
        self.k = k
        self.m = m
        self.dt = dt
        self.rho = rho
        self.Cd = Cd
        self.A = A
        self.l0 = l0

        self.t.append(0)
        self.ay.append(-self.g)
        self.vy.append(0)
        self.y.append(h0)

        self.Ep = []
        self.Ek = []
        self.Eel = []
        self.Euk = []

        # prije skoka
        self.Ep.append(m*(self.g)*(self.y[-1]))
        self.Ek.append(0)
        self.Eel.append(0)
        self.Euk.append(self.Ep[-1] + self.Ek[-1] + self.Eel[-1])


    def a_prije_bez(self, y, v, t):
        return - self.g

    def a_poslije_bez(self, y, v, t):
        return - self.g + (self.k/self.m)*(self.h0 - self.y[-1] - self.l0)


    def __move_bez(self, dt, akc):
        self.t.append(self.t[-1] + dt)

        self.ay.append(akc(self.y[-1], self.vy[-1], self.t[-1]))
        self.vy.append(self.vy[-1] + self.ay[-1]*dt)
        self.y.append(self.y[-1] + self.vy[-1]*dt)

        self.Ep.append(self.m*(self.g)*(self.y[-1]))
        self.Ek.append(0.5*self.m*(self.vy[-1])**2)

        if self.y[-1] > self.h0 - self.l0:
            self.Eel.append(0)
        else:
            self.Eel.append(0.5*self.k*(self.h0 - self.y[-1] - self.l0)**2)

        self.Euk.append(self.Ep[-1] + self.Ek[-1] + self.Eel[-1])


    def prijeposlije_bez(self, dt):
        if self.y[-1] > self.h0 - self.l0:
            self.__move_bez(dt, self.a_prije_bez)
        else:
            self.__move_bez(dt, self.a_poslije_bez)


    def range_bez(self, dt, tuk):
        while self.t[-1] <= tuk:
            self.prijeposlije_bez(dt)
        return self.t, self.y, self.Euk, self.Ep, self.Ek, self.Eel



    
    def a_prije(self, y, v, t):
        # - g - otpor zraka
        return - self.g - ((self.rho*self.Cd*self.A)/(2*self.m))*(self.vy[-1])*abs(self.vy[-1])

    def a_poslije(self, y, v, t):
        # - g + otpor zraka + konop
        return - self.g - ((self.rho*self.Cd*self.A)/(2*self.m))*(self.vy[-1])*abs(self.vy[-1]) + (self.k/self.m)*(self.h0 - self.y[-1] - self.l0)



    def __move(self, dt, akceleracija):
        self.t.append(self.t[-1] + dt)

        self.ay.append(akceleracija(self.y[-1], self.vy[-1], self.t[-1]))
        self.vy.append(self.vy[-1] + self.ay[-1]*dt)
        self.y.append(self.y[-1] + self.vy[-1]*dt)


        self.Ep.append(self.m*(self.g)*(self.y[-1]))
        self.Ek.append(0.5*self.m*(self.vy[-1])**2)
        
        if self.y[-1] > self.h0 - self.l0:
            self.Eel.append(0)
        else:
            self.Eel.append(0.5*self.k*(self.h0 - self.y[-1] - self.l0)**2)

        self.Euk.append(self.Ep[-1] + self.Ek[-1] + self.Eel[-1])


    def prijeposlije(self, dt):
        if self.y[-1] > self.h0 - self.l0:
            self.__move(dt, self.a_prije)
        else:
            self.__move(dt, self.a_poslije)

    
    def range(self, dt, tuk):
        while self.t[-1] <= tuk:
            self.prijeposlije(dt)
        return self.t, self.y, self.Euk, self.Ep, self.Ek, self.Eel

