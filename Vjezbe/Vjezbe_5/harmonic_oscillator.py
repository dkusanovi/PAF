import math
import matplotlib.pyplot as plt

class HarmonicOscillator:

    def __init__(self, v0, x0, k, m, dt):
        self.x = []
        self.t = []
        self.vx = []
        self.ax = []
        self.g = 9.81
        self.v0 = v0
        self.x0 = x0
        self.k = k
        self.m = m
        self.dt = dt


    def set_initial_conditions(self, v0, theta, x0, k, m, dt):
        theta = (theta/180)*math.pi
        self.theta = theta
        self.v0 = v0
        self.x0 = x0
        self.k = k
        self.m = m
        self.dt = dt

        self.t.append(0)
        self.x.append(0)
        self.vx.append(v0*(math.cos(self.theta)))
        self.ax.append(0)


    def reset(self):
        self.__init__(self.v0, self.theta, self.x0, self.k, self.m)


    def oscillate(self, t):
        for i in range(int(t/self.dt)):
            self.t.append(self.t[-1] + self.dt)
            self.ax.append(-(self.k/self.m)*self.x[-1])
            self.vx.append(self.vx[-1] + self.ax[-1]*self.dt)
            self.x.append(self.x[-1] + self.vx[-1]*self.dt)

        return self.t, self.x


    def graf(self):
        self.oscillate(2)
        fig, axes = plt.subplots(1, 3, figsize=(13, 4))

        axes[0].plot(self.t, self.x)
        axes[0].set_title("x-t graf")
        axes[0].set_ylabel('put (m)')
        axes[0].set_xlabel('vrijeme (s)')

        axes[1].plot(self.t, self.vx)
        axes[1].set_title("v-t graf")
        axes[1].set_ylabel('brzina (m/s)')
        axes[1].set_xlabel('vrijeme (s)')

        axes[2].plot(self.t, self.ax)
        axes[2].set_title("a-t graf")
        axes[2].set_ylabel('akceleracija (m/s^2)')
        axes[2].set_xlabel('vrijeme (s)')
        
        plt.show()


    def preciznost(self):
        self.oscillate(2) # za graf u zdk1 slican lissajousovim krivuljama, umjesto 2 stavimo 15
        return self.t, self.ax, self.vx, self.x


    def period_n(self, t):
        self.t, self.x = self.oscillate(t)

        A = max(self.x)
        i = self.x.index(A)
        j = self.t[i]

        T = j*4

        print(T)


    def period_a(self):
        T = 2*math.pi*math.sqrt(self.m/self.k)
        print(T)
        